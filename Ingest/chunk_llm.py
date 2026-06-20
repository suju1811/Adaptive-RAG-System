import os
import glob
import asyncio
import warnings
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from meta_llm import get_chunk_instruction
from tqdm.asyncio import tqdm_asyncio
from tenacity import retry, stop_after_attempt, wait_exponential
from openai import RateLimitError,APIConnectionError,APITimeoutError,BadRequestError
from langchain_core.exceptions import OutputParserException
from Ingest.constants import KNOWLEDGE_BASE,MODEL

# ── Filter pydantic serialization warnings ─────────────────────────────────────
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="pydantic"
)

load_dotenv(override=True)
openai = OpenAI()

wait = wait_exponential(multiplier=1, min=1, max=20)
stop = stop_after_attempt(3)
WORKERS = 4    # max concurrent API calls — acts as semaphore limit

CHUNK_SYSTEM_PROMPT = """\
You are a precise document chunking specialist. Your sole responsibility is to \
split documents into well-structured, semantically complete chunks following \
the exact instructions provided.

You will receive:
1. A document to chunk
2. Specific chunking instructions tailored to the document's domain and structure

Core rules:
- Follow the chunking instructions exactly — do not deviate or apply generic defaults
- Every chunk must be semantically self-contained and independently meaningful
- Never split mid-sentence, mid-table-row, mid-bullet-item, or mid-entity-ID
- Preserve all original text verbatim — do not alter, paraphrase, or rewrite
- Do not add any content, commentary, or explanation to your output

You must output valid JSON matching the required schema. \
No explanation, no preamble, no markdown fences outside the JSON.
"""

# ── Pydantic models ─────────────────────────────────────────────────────────────

class Result(BaseModel):
    page_content: str
    metadata: dict

class Entity(BaseModel):
    name: str = Field(
        description="The name or label of the entity as it appears in the text"
    )
    type: str = Field(
        description="The category or type of this entity as relevant to the "
                    "document's domain — infer from context (e.g. Person, "
                    "Organisation, Product, Event, Location, Concept, or any "
                    "domain-specific category present in the document)"
    )
    id: str | None = Field(
        default=None,
        description="Unique identifier for this entity if one exists in the text "
                    "— such as a code, reference number, or key. None if not present"
    )

class Relationship(BaseModel):
    source: str = Field(
        description="The name or ID of the source entity in this relationship"
    )
    relation: str = Field(
        description="The relationship type expressed as a short verb phrase — "
                    "infer from the document context (e.g. manages, depends_on, "
                    "located_in, authored_by, part_of, references)"
    )
    target: str = Field(
        description="The name or ID of the target entity in this relationship"
    )

class Chunk(BaseModel):
    headline: str = Field(
        description="A concise 3-7 word retrieval-optimised phrase that captures "
                    "the core subject of this chunk — written as the most likely "
                    "search query a user would type to find this content"
    )
    summary: str = Field(
        description="2-4 sentences capturing the key facts, named entities, and "
                    "relationships in this chunk — written to directly answer "
                    "likely user questions without needing surrounding context"
    )
    original_text: str = Field(
        description="The exact verbatim text of this chunk from the source document "
                    "— not altered, summarised, paraphrased, or cleaned up in any way"
    )
    source_section: str = Field(
        description="The heading path indicating where in the document this chunk "
                    "came from, using the format: 'Parent Section > Child Section'. "
                    "Use only the actual heading text from the document"
    )
    entities: list[Entity] = Field(
        default_factory=list,
        description="All named entities identified in this chunk — people, "
                    "organisations, products, concepts, or any domain-specific "
                    "objects. Empty list if none found"
    )
    relationships: list[Relationship] = Field(
        default_factory=list,
        description="Relationships between entities identified within this chunk. "
                    "Only include relationships where both source and target "
                    "are present in this chunk. Empty list if none found"
    )
    chunk_index: int = Field(
        description="Zero-based sequential position of this chunk within the "
                    "document — first chunk is 0, second is 1, no gaps allowed"
    )

    def as_result(self, source: str, doc_type: str) -> Result:
        entity_ids   = [e.id for e in self.entities if e.id]
        entity_types = list(set([e.type for e in self.entities]))

        metadata = {
            "source":            source,
            "doc_type":          doc_type,
            "source_section":    self.source_section,
            "chunk_index":       self.chunk_index,
            "has_relationships": len(self.relationships) > 0,
        }
        # Chroma rejects empty metadata lists — only include when populated
        if entity_ids:
            metadata["entity_ids"] = entity_ids
        if entity_types:
            metadata["entity_types"] = entity_types

        return Result(
            page_content=(
                self.headline + "\n\n" +
                self.summary  + "\n\n" +
                self.original_text
            ),
            metadata=metadata,
        )

class Chunks(BaseModel):
    chunks: list[Chunk] = Field(
        description="Ordered list of all chunks produced from the document, "
                    "indexed from 0 with no gaps"
    )


# ── LLM — created ONCE at module level, shared across all async calls ──────────
_llm = ChatOpenAI(model=MODEL, temperature=0)
_structured_llm = _llm.with_structured_output(Chunks)


# ── Document loader ─────────────────────────────────────────────────────────────

def fetchCunkDocument():
    """Loads all non-README markdown files from the knowledge base directory."""

    documents = []

    files = os.path.join(KNOWLEDGE_BASE, "*.md")
    file_paths = [
        p for p in glob.glob(files)
        if os.path.basename(p).lower() != "readme.md"
    ]

    for file_path in file_paths:
        doc_type  = Path(file_path).stem
        file_name = os.path.basename(file_path)

        if os.path.exists(file_path):
            loader   = TextLoader(file_path, encoding="utf-8")
            doc_list = loader.load()
            doc      = doc_list[0]

            doc.metadata.update({
                "doc_type":  doc_type,
                "file_name": file_name
            })
            documents.append(doc)
        else:
            print(f"[fetchCunkDocument] WARNING: {file_name} not found at {file_path}")

    return documents


# ── User prompt builder ─────────────────────────────────────────────────────────

def create_chunk_user_prompt(document, instruction) -> str:
    chunk_user_prompt = f"""\
        Chunk the following document according to the instructions below.

        {instruction}

        ---

        DOCUMENT CONTEXT:
        - Document Type: {document.metadata.get("doc_type", "unknown")}
        - Source: {document.metadata.get("source", "unknown")}

        ---

        Here is the document:

        {document.page_content}
        """
    return chunk_user_prompt


# ── Single document chunker — async with retry ──────────────────────────────────
# Uses asyncio.Semaphore to cap concurrent API calls at WORKERS (default 4).
# .ainvoke() is the non-blocking async equivalent of .invoke() — releases
# control while waiting for the API response so other coroutines can run.

@retry(wait=wait, stop=stop)
async def get_chunks(document, instruction, semaphore: asyncio.Semaphore):
    file_name = document.metadata.get("file_name", "unknown")
    async with semaphore:  
        try:                      # limit concurrent API calls
            messages = [
                {"role": "system", "content": CHUNK_SYSTEM_PROMPT},
                {"role": "user",   "content": create_chunk_user_prompt(document, instruction)}
            ]

            response = await _structured_llm.ainvoke(messages)   # non-blocking API call

            source   = document.metadata.get("source")
            doc_type = document.metadata.get("doc_type")
            return {
                "file_name": file_name,
                "chunks":[
                    chunk.as_result(source=source, doc_type=doc_type)
                    for chunk in response.chunks
                ],
                "error": None
            }

        except RateLimitError as e:
            print(f"[get_chunks] Rate limit hit for {file_name} — retrying...")
            raise
        except APITimeoutError as e:
            print(f"[get_chunks] Timeout for {file_name} — retrying...")
            raise

        except APIConnectionError as e:
            print(f"[get_chunks] Connection error for {file_name} — retrying...")
            raise

        except OutputParserException as e:
            print(f"[get_chunks] Schema mismatch for {file_name}: {e}")
            return {"file_name": file_name, "chunks": [], "error": str(e)}

        except BadRequestError as e:
            print(f"[get_chunks] Bad request for {file_name}: {e}")
            return {"file_name": file_name, "chunks": [], "error": str(e)}
        except Exception as e:
            print(f"[get_chunks] Unexpected error for {file_name}: {type(e).__name__}: {e}")
            return {"file_name": file_name, "chunks": [], "error": str(e)}


# ── Async orchestrator ──────────────────────────────────────────────────────────
# Fires all document chunking tasks concurrently within the semaphore limit.
# tqdm_asyncio.gather shows a live progress bar as each document completes.

async def create_chunks_async(documents, chunk_instruction):
    semaphore = asyncio.Semaphore(WORKERS)       # shared across all tasks

    tasks = [
        get_chunks(doc, chunk_instruction, semaphore)
        for doc in documents
    ]

    results = await tqdm_asyncio.gather(*tasks, desc="Chunking documents")

    chunks = []
    failures = []

    for res in results:
        if res["error"]:
            failures.append({
                "file_name": res["file_name"],
                "reason": res["error"]
            })
        else:
            chunks.extend(res["chunks"])
    
    #print for server debug
    print(f"\n[create_chunks] {len(chunks)} chunks created from "
          f"{len(documents) - len(failures)}/{len(documents)} files")
    if failures:
        print(f"[create_chunks] {len(failures)} file(s) failed:")
        for f in failures:
            print(f" ERROR: {f['file_name']} — {f['reason']}")
    
    return chunks,failures


def create_chunks():
    documents = fetchCunkDocument()
    print("[create_chunks] fetching instruction for chunking...")
    chunk_instruction = get_chunk_instruction()
    if chunk_instruction is None:
        print("[create_chunks] ERROR: meta LLM failed to generate chunking instructions — aborting")
        return [], [{"file_name": "ALL", "reason": "Meta LLM failed — no chunking instructions generated"}]
    else:
        print("[create_chunks] chunk instruction fetched successfully")

    return asyncio.run(create_chunks_async(documents, chunk_instruction))