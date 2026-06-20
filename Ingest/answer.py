from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from chromadb import PersistentClient
from tenacity import retry, wait_exponential, stop_after_attempt
from pydantic import BaseModel
from openai import RateLimitError,APIConnectionError,APITimeoutError,BadRequestError
from Ingest.constants import DB_PATH,COLLECTION_NAME,EMBEDDING_MODEL,MODEL,RETRIEVAL_K,MAX_CONTEXT_CHARS

load_dotenv(override=True)
openai = OpenAI()

_rewrite_llm = ChatOpenAI(model=MODEL, temperature=0)
_answer_llm = ChatOpenAI(model=MODEL, temperature=0)

try:
    _chroma = PersistentClient(path=DB_PATH)
    _collection = _chroma.get_or_create_collection(COLLECTION_NAME)
except Exception as e:
    print(f"[fetch_context_knowledge_base] Chroma connection error: {e}")

SYSTEM_PROMPT = """
You are a knowledgeable assistant for an Adaptive Knowledge Intelligence system.
You answer questions based strictly on the provided knowledge base context.
Your answer will be evaluated for accuracy, relevance, and completeness — answer only what is asked and answer it fully.
If the answer is not present in the context, say so clearly — do not guess or infer beyond what is provided.
Always cite which document or section your answer comes from.

If the user's message is a greeting, farewell, or general conversational message (e.g. "Hi", "Thanks", "Goodbye"), 
respond naturally and briefly without referencing the knowledge base or context at all.

Here are the relevant extracts from the Knowledge Base:
{context}

With this context, please answer the user's question accurately, completely, and with proper citations.
"""

class Result(BaseModel):
    page_content: str
    metadata: dict

wait = wait_exponential(multiplier=1, min=1, max=20)
stop = stop_after_attempt(3)

def format_history(history):
    """Convert list of role/content dicts to readable conversation string."""
    lines = []
    for msg in history:
        role = "User" if msg.get("role") == "user" else "Assistant"
        content = msg.get("content", "")
        lines.append(f"{role}: {content}")
    return "\n".join(lines) if lines else "No previous conversation."

@retry(wait=wait,stop=stop)
def rewrite_query(question, history=[]):
    recent_history = format_history(history[-6:])

    prompt = f"""
        You are helping search a knowledge base to answer a user question.

        Conversation so far (latest):
        {recent_history}

        Current question:
        {question}

        If the question is ambiguous or references something from history \
        (e.g. "it", "that", "they"), rewrite it as a standalone self-contained question.
        If the question is already clear and specific, return it exactly as is.

        IMPORTANT: Respond ONLY with the question, nothing else.
        """
    
    try:
        response = _rewrite_llm.invoke([{"role":"user","content":prompt}])
        
        rewritten = response.content.strip()
        return rewritten if rewritten else question
    except RateLimitError as e:
        print(f"[rewrite_query] Rate limit hit — retrying...")
        raise
    except APITimeoutError as e:
        print(f"[rewrite_query] Timeout error — retrying...")
        raise
    except APIConnectionError as e:
        print(f"[rewrite_query] Connection error — retrying...")
        raise
    except BadRequestError as e:
        print(f"[rewrite_query] Bad request error: {e}")
        return question
    except Exception as e:
        print(f"[rewrite_query] Unexpected error : {type(e).__name__}: {e}")
        return question


def fetch_context_knowledge_base(question):
    try:
        query = openai.embeddings.create(model=EMBEDDING_MODEL, input=[question])
        query_vector = query.data[0].embedding
    except RateLimitError as e:
        print(f"[fetch_context_knowledge_base] Rate limit on embedding — {e}")
        return []
    except APITimeoutError as e:
        print(f"[fetch_context_knowledge_base] Embedding API Timeout error — {e}")
        return []
    except APIConnectionError as e:
        print(f"[fetch_context_knowledge_base] Embedding API Connection error — {e}")
        return []
    except Exception as e:
        print(f"[fetch_context_knowledge_base] Embedding failed — {type(e).__name__}: {e}")
        return []

    try:
        results = _collection.query(query_embeddings=[query_vector], n_results=RETRIEVAL_K)
    except Exception as e:
        print(f"[fetch_context_knowledge_base] Chroma collection not found or chunk retrieval failed — aborting similarity vector search: {e}")
        return []
    chunks = []
    
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    for res in zip(documents,metadatas):
        chunks.append(Result(page_content=res[0],metadata=res[1]))
    return chunks

def merge_chunks(chunks_original, chunks_rewritten):
    merged = chunks_original[:]

    existing = {
        chunk.page_content
        for chunk in chunks_original
    }

    for chunk in chunks_rewritten:
        if chunk.page_content not in existing:
            merged.append(chunk)
            existing.add(chunk.page_content)

    return merged

def fetch_context(question,history=[]):

    try:
        rewritten_query = rewrite_query(question,history)
    except Exception as e:
        print(f"[fetch_context] Query rewrite failed: {e}")
        rewritten_query = question

    chunks_original = fetch_context_knowledge_base(question)
    chunks_rewritten = fetch_context_knowledge_base(rewritten_query)

    chunks = merge_chunks(chunks_original,chunks_rewritten)

    return chunks

def make_rag_messages(question, history, chunks):
    context = "\n\n".join(
        f"""
        Source: {chunk.metadata.get('source','Unknown')}
        Type: {chunk.metadata.get('type','Unknown')}

        {chunk.page_content}
        """ for chunk in chunks
    )
    context = context[:MAX_CONTEXT_CHARS]
    system_prompt = SYSTEM_PROMPT.format(context=context)
    return (
        [{"role": "system", "content": system_prompt}]
        + history
        + [{"role": "user", "content": question}]
    )

@retry(wait=wait, stop=stop)
def answer_question(question: str, history: list[dict] = []) -> tuple[str, list]:
    chunks = fetch_context(question,history)
    if not chunks:
        return (
            "I couldn't find relevant information in the existing knowledge base.",
            []
        )
    messages = make_rag_messages(question,history,chunks)
    try:
        response = _answer_llm.invoke(messages)
        return response.content.strip(),chunks
    except RateLimitError as e:
        print(f"[rewrite_query] Rate limit hit — retrying...")
        raise
    except APITimeoutError as e:
        print(f"[answer_question] Timeout error — retrying...")
        raise
    except APIConnectionError as e:
        print(f"[answer_question] Connection error — retrying...")
        raise
    except BadRequestError as e:
        print(f"[answer_question] Bad request error: {e}")
        return "",chunks
    except Exception as e:
        print(f"[answer_question] Unexpected error : {type(e).__name__}: {e}")
        return "",chunks

if __name__ == "__main__":
    response,chunks = answer_question("Who reports directly to the CEO?",[])
    print(response)
    print(chunks)