from httpx import delete
from numpy import append
from chunk_llm import create_chunks
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
from chromadb import PersistentClient
from openai import RateLimitError,APIConnectionError,APITimeoutError
from Ingest.constants import DB_PATH,EMBEDDING_MODEL,EMBEDDING_BATCH,COLLECTION_NAME

load_dotenv(override=True)

openai = OpenAI()

def create_embeddings_batch(texts: list[str]) -> list[list[float]]:
    """
    Embeds texts in batches to avoid hitting OpenAI's per-request token limit.
    Returns flat list of embedding vectors in the same order as input texts.
    """
    vectors = []

    for i in range(0, len(texts), EMBEDDING_BATCH):
        batch = texts[i : i + EMBEDDING_BATCH]
        try:
            response = openai.embeddings.create(
                model=EMBEDDING_MODEL,
                input=batch
            )
            vectors.extend([e.embedding for e in response.data])

        except RateLimitError as e:
            print(f"[create_embeddings_batch] Rate limit hit on batch {i // EMBEDDING_BATCH + 1} — {e}")
            raise

        except APITimeoutError as e:
            print(f"[create_embeddings_batch] Timeout on batch {i // EMBEDDING_BATCH + 1} — {e}")
            raise

        except APIConnectionError as e:
            print(f"[create_embeddings_batch] Connection error on batch {i // EMBEDDING_BATCH + 1} — {e}")
            raise

        except Exception as e:
            print(f"[create_embeddings_batch] Unexpected error on batch "
                  f"{i // EMBEDDING_BATCH + 1}: {type(e).__name__}: {e}")
            raise

    return vectors

def create_embedding(chunks):
    """
    Embeds all chunks and stores them in ChromaDB.
    Deletes existing collection if present to ensure clean re-ingestion.
    """
    try:
        # ── Connect to Chroma ───────────────────────────────────────────
        chroma = PersistentClient(path=DB_PATH)

        # drop and recreate collection for clean re-ingestion
        if COLLECTION_NAME in [c.name for c in chroma.list_collections()]:
            chroma.delete_collection(COLLECTION_NAME)
            print(f"[create_embedding] Existing collection '{COLLECTION_NAME}' dropped")

        collection = chroma.get_or_create_collection(COLLECTION_NAME)

    except Exception as e:
        print(f"[create_embedding] Failed to connect to ChromaDB — {type(e).__name__}: {e}")
        return False

    # ── Embed in batches ────────────────────────────────────────────────
    texts = [chunk.page_content for chunk in chunks]
    ids    = [str(i) for i in range(len(chunks))]
    metas  = [chunk.metadata for chunk in chunks]

    try:
        vectors = create_embeddings_batch(texts)
    except Exception as e:
        print(f"[create_embedding] Embedding failed — aborting ingestion: {e}")
        return False

    # ── Store in Chroma ─────────────────────────────────────────────────
    try:
        collection.add(
            ids        = ids,
            embeddings = vectors,
            documents  = texts,
            metadatas  = metas
        )
        print(f"[create_embedding] Vector store created with {collection.count()} documents")
        return True

    except Exception as e:
        print(f"[create_embedding] Failed to store chunks in ChromaDB — {type(e).__name__}: {e}")
        return False


if __name__ == "__main__":

    chunks,failures = create_chunks()
    if not chunks:
        print("Pipeline aborted: Chunking Failed.")
        exit(1)

    success = create_embedding(chunks)

    if success:
        print("\nIngestion completed successfully!")
    else:
        print("\nIngestion failed check errors!")
        exit(1)