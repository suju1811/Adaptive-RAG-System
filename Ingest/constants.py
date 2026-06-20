from pathlib import Path

#Project paths
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "DATA"
KNOWLEDGE_BASE = str(DATA_DIR/"knowledge_base")
DB_PATH = str(ROOT_DIR / "DB")

#Model and embedding constants
MODEL = "gpt-5-nano"
EMBEDDING_MODEL = "text-embedding-3-large"
EMBEDDING_BATCH = 100
COLLECTION_NAME = "AR_VECTOR_STORE"

RETRIEVAL_K = 5
MAX_CONTEXT_CHARS = 2500