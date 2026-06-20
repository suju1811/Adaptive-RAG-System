# 🏢 Adaptive RAG System

A full-stack AI pipeline that turns any collection of documents into a queryable knowledge base — automatically. Upload documents, and the system discovers the domain, configures its own chunking strategy, builds a vector store, and answers natural-language questions with cited, context-grounded responses.

Built as a learning project covering RAG fundamentals, LLM-driven pipeline configuration, async document processing, and conversational AI — with a roadmap toward Graph RAG and a fully generic multi-tenant platform.

---

## How It Works

```
Documents (Markdown)
        ↓
Meta LLM — reads README + file metadata
        → generates domain-aware chunking instructions
        ↓
Chunking LLM — splits each document into structured chunks
        → headline · summary · original text · entities · relationships
        ↓
ChromaDB — embeds and stores chunks as vectors
        ↓
Query → rewrite → retrieve → rerank → LLM answer with citations
```

---

## Project Structure

```
Adaptive RAG Research/
├── app.py                  # Gradio chat UI
├── DATA/
│   └── knowledge_base/     # Place your .md documents here
│       └── README.md       # Describes your knowledge base to the system
├── DB/                     # ChromaDB vector store (auto-generated)
├── Ingest/
│   ├── constants.py        # All config — models, paths, DB names
│   ├── meta_llm.py         # Generates chunking instructions from metadata
│   ├── chunk_llm.py        # Chunks documents using LLM + async pipeline
│   ├── ingest.py           # Orchestrates ingestion end-to-end
│   └── answer.py           # Query rewriting, retrieval, and answer generation
└── pyproject.toml
```

---

## Phases

| Phase | Status | Description |
|-------|--------|-------------|
| 1 — Simple RAG | ✅ Complete | Meta LLM config → LLM chunking → vector store → Q&A chat |
| 2 — Graph RAG | 🔜 Planned | Entity extraction → knowledge graph → hybrid retrieval |
| 3 — Generic Platform | 🔜 Planned | File upload UI · adaptive pipeline · agentic tools |

---

## Setup

### Prerequisites
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key

### 1. Clone the repo

```bash
git clone https://github.com/your-username/adaptive-rag-research.git
cd adaptive-rag-research
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-...
```

### 4. Add your documents

Place your `.md` files inside `DATA/knowledge_base/`. Include a `README.md` in that folder describing your knowledge base — the system reads it to configure the chunking pipeline automatically.

A sample corporate knowledge base (Northstar Dynamics) is included to get started.

### 5. Run ingestion

```bash
uv run Ingest/ingest.py
```

This runs the full pipeline — meta LLM generates chunking instructions, documents are chunked concurrently, embeddings are created and stored in ChromaDB.

### 6. Launch the chat UI

```bash
uv run app.py
```

Opens the Gradio chat interface at `http://127.0.0.1:7860`.

---

## Configuration

All settings are in `constants.py`:

---

## Key Design Decisions

**Meta LLM driven chunking** — rather than hardcoding a chunking strategy, the system reads your document metadata and generates domain-specific instructions on the first run. Works equally well for HR records, legal contracts, medical notes, or technical docs.

**Async chunking pipeline** — documents are chunked concurrently using `asyncio` with a semaphore to respect API rate limits. Processing 4 documents takes the same time as processing 1.

**Enriched chunks** — each chunk carries a headline, summary, original text, extracted entities, and relationships. The summary is embedded for richer semantic retrieval; the original text is returned for accurate citations.

**Query rewriting** — user questions are rewritten into precise search queries before retrieval, resolving ambiguous references from conversation history.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | OpenAI via LangChain |
| Embeddings | OpenAI `text-embedding-3-large` |
| Vector store | ChromaDB (persistent) |
| UI | Gradio |
| Package manager | uv |
| Retry / resilience | Tenacity |

---

## Sample Knowledge Base

The repo includes a synthetic corporate dataset for **Northstar Dynamics** — 4 interconnected markdown files covering HR, projects, risks, and vendors with cross-referenced entities and relationships. Useful for testing multi-hop queries.

---

## License

MIT