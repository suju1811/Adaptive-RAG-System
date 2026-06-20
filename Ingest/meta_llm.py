#Meta LLM generates the system propmt and the instruction for chunking the document
#which is used in decument pre-processing method of chunking the document

import os
import glob
import re
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
import warnings
from openai import RateLimitError, APITimeoutError, APIConnectionError, BadRequestError
from langchain_core.exceptions import OutputParserException
from Ingest.constants import KNOWLEDGE_BASE, MODEL

#filter pydantic serialized warnings
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="pydantic"
)

load_dotenv(override=True)
openai = OpenAI()


# Metadata header regex
_METADATA_HEADER_RE = re.compile(
    r"^#{1,6}\s+.*\b(metadata|about|overview|file\s+info|document\s+info|doc\s+info)\b.*$",
    re.IGNORECASE,
)
# Horizontal rule separator
_HR_RE = re.compile(r"^(\*\s*){3,}$|^(-\s*){3,}$|^(_\s*){3,}$")

META_SYSTEM_PROMPT = """\
You are an expert RAG pipeline architect specialising in document intelligence \
and knowledge base design.

Your sole responsibility is to analyse a set of document metadata summaries ,readme file and \
produce precise, actionable instructions that will guide a downstream chunking \
process. You are not answering questions about the documents — you are designing \
the ingestion strategy for them.

When analysing the provided metadata, you must:
1. Identify the domain, industry, and document types present
2. Understand the entity types, relationship types, and ID schemes used
3. Determine the structural patterns across the files (tables, bullet lists, \
prose, headings, code blocks)
4. Infer how documents cross-reference each other
5. Decide the optimal chunking boundaries so that each chunk is semantically \
complete and self-contained

Your output will be consumed directly by a chunking LLM — it must be concrete, \
specific, and unambiguous. Never use vague instructions like "chunk appropriately" \
or "use reasonable size". Always give explicit rules.

Do NOT include any instructions about output format, JSON structure, schema, \
or how the chunking LLM should return its results — output format is enforced \
separately by the pipeline and is not your concern.

You must output valid JSON matching the required schema. No explanation, no \
preamble, no markdown fences outside the JSON.
"""

# Pydantic model for instruction and system prompt for the chunking process
class ChunkingInstructions(BaseModel):
    instruction: str = Field(
        description="The instruction for the chunking LLM — specifies exactly "
                    "how to split, label, and structure chunks from the documents"
    )


def fetchMetaDocument():
    """
    Fetches two categories of content from the knowledge base:

    1. README.md  — loaded in full as a single Document
                    doc_type = "readme"

    2. Data files — extract the document metadata block.
                    Fallback: if no metadata block exists, the first 150 lines
                    of the file are returned so the meta-prompt LLM still has
                    enough structural context to work with.
                    doc_type = stem of the filename (e.g. "hr_directory")

    Returns:
        list[Document]  each with .page_content and .metadata keys:
                        - doc_type          : "readme" | filename stem
                        - source            : absolute file path
                        - file_name         : basename of the file
                        - extraction_method : "metadata_block" | "top_100_lines"
    """
    documents = []

    # ------------------------------------------------------------------ #
    # 1.  README  — load the whole file                                   #
    # ------------------------------------------------------------------ #
    readme_path = os.path.join(KNOWLEDGE_BASE, "README.md")

    if os.path.exists(readme_path):
        loader = TextLoader(readme_path, encoding="utf-8")
        readme_docs = loader.load() # returns a list with one Document

        # TextLoader already sets metadata["source"]; we add our own keys
        readme_doc = readme_docs[0]
        readme_doc.metadata.update({
            "doc_type":  "readme",
            "file_name": "README.md",
            "extraction_method": "readme_file",
        })
        documents.append(readme_doc)
    else:
        print(f"[fetchMetaDocument] WARNING: README.md not found at {readme_path}")

    # ------------------------------------------------------------------ #
    # 2.  Data files — extract only the ## Document Metadata block        #
    # ------------------------------------------------------------------ #
    # Collect every .md that is NOT the README
    md_pattern = os.path.join(KNOWLEDGE_BASE, "*.md")
    data_files = [
        p for p in glob.glob(md_pattern)
        if os.path.basename(p).lower() != "readme.md"
    ]

    for file_path in sorted(data_files):           # sorted = deterministic order
        metadata_text, extraction_method = _extract_metadata_block(file_path)

        file_name = os.path.basename(file_path)
        doc_type  = Path(file_path).stem          # e.g. "hr_directory"

        doc = Document(
            page_content=metadata_text,
            metadata={
                "doc_type":          doc_type,
                "source":            file_path,
                "file_name":         file_name,
                "extraction_method": extraction_method,   # "metadata_block" | "top_100_lines"
            },
        )
        documents.append(doc)
    
    return documents


def _extract_metadata_block(file_path: str) -> tuple[str, str]:
    """
    Reads a markdown file and attempts to return the metadata block

    Fallback: if no metadata heading is found, returns the first
    100 lines of the file so the meta-prompt LLM still has enough structural
    context to infer domain, entities, and chunking strategy.

    Returns:
        tuple(content: str, extraction_method: str)
            extraction_method is "metadata_block" or "top_150_lines"
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # --- Primary: regex scan for any metadata-like heading ---
    start_index = None
    matched_heading = None
    for i, line in enumerate(lines):
        if _METADATA_HEADER_RE.match(line.strip()):
            start_index = i
            matched_heading = line.strip()
            break

    if start_index is not None:
        # Collect from the matched heading up to the next separator
        # or the next same-or-higher-level heading (whichever comes first)
        block_lines = []
        for j, line in enumerate(lines[start_index:]):
            if j > 150:
                break
            # Stop at a horizontal rule separator
            if j > 0 and _HR_RE.match(line.strip()):
                break
            # Stop if we hit another heading of equal or higher level
            if j > 0 and re.match(r"^#{1,6}\s+", line):
                break
            block_lines.append(line)
        return "".join(block_lines).strip(), "metadata_block"

    # --- Fallback: no metadata block found, return top 150 lines ---
    print(
        f"[fetchMetaDocument] INFO: no metadata block are present"
        f"{os.path.basename(file_path)} — falling back to top 150 lines"
    )
    fallback_text = "".join(lines[:150]).strip()
    return fallback_text, "top_100_lines"

def create_meta_user_prompt(documents: list[Document]) -> str:

    readme_content = "No Readme Found"
    summaries = []
    file_count = 0

    for doc in documents:
        if doc.metadata.get("doc_type") == "readme":
            readme_content = doc.page_content
        else:
            file_count += 1
            file_name = doc.metadata.get("file_name","unknown")
            extraction_method = doc.metadata.get("extraction_method","unknown")

            # Flag fallback extractions so the LLM knows this is less structured
            metadata_note = (
                "" if extraction_method == "metadata_block"  
                else "[no metadata block found — showing top of file as fallback]"
            )

            summary_block = (
                f"###{file_name}{metadata_note}"
                f"{doc.page_content}"
            )

            summaries.append(summary_block)
    
    meta_user_prompt = f"""\
            Below is the README and per-file metadata for a knowledge base that needs to \
            be ingested into a RAG pipeline.

            First, reason about the knowledge base:
            - What domain and industry is this data from?
            - What are the key entity types and how are they identified?
            - How do documents cross-reference each other?
            - What structural patterns exist (tables, bullet lists, prose, headings)?
            - What kinds of questions will users ask against this data?

            Then, using that understanding, generate chunking instructions that specify:
            - The primary split strategy (by markdown heading level, by paragraph, \
            by sentence, sliding window, or semantic boundary)
            - Exactly which heading levels to split on (e.g. split on ## and ###, \
            never split within ###)
            - Chunk size target in tokens and overlap in tokens
            - How to handle tables (keep whole or split by row)
            - How to handle bullet lists (keep whole or split by item)
            - Any domain-specific rules — entity ID preservation, cross-reference \
            handling, special structural patterns unique to this data

            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            README
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            {readme_content}

            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            FILE METADATA SUMMARIES ({file_count} files)
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            {summaries}

            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            Based on the above, generate the chunking instructions.
            Remember: be explicit and specific — no vague guidance.
            """
    return meta_user_prompt

def get_chunk_instruction() -> str | None:

    """
    Calls the meta LLM to generate chunking instructions.
    
    Returns:
        instruction string on success
        None on failure — caller must handle this
    """

    try:
    
        documents = fetchMetaDocument()

        messages = [
            {"role": "system", "content": META_SYSTEM_PROMPT},
            {"role": "user", "content": create_meta_user_prompt(documents)}
        ]

        llm = ChatOpenAI(
            model=MODEL,
            temperature=0
        )

        structured_llm = llm.with_structured_output(ChunkingInstructions)
        response = structured_llm.invoke(messages)

        return response.instruction
    
    except RateLimitError as e:
        print(f"[get_chunk_instruction] Rate limit hit — {e}")
        return None

    except APITimeoutError as e:
        print(f"[get_chunk_instruction] Request timed out — {e}")
        return None

    except APIConnectionError as e:
        print(f"[get_chunk_instruction] Connection error — {e}")
        return None

    except BadRequestError as e:
        print(f"[get_chunk_instruction] Bad request — {e}")
        return None

    except OutputParserException as e:
        print(f"[get_chunk_instruction] LLM response did not match schema — {e}")
        return None

    except Exception as e:
        print(f"[get_chunk_instruction] Unexpected error — {type(e).__name__}: {e}")
        return None