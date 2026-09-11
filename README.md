# 🚀 Enterprise Local RAG Assistant

> Production-ready Local Retrieval-Augmented Generation (RAG) System using FAISS, Sentence Transformers and Quantized Local LLMs (GGUF)

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FAISSs.io/badge/FAISS-VectorDB-green
![RAG](https://img.shields.io/badge/cture-RAG-red
![LLM](https://img.shields.io/badge/LLM-Qwen2.5-orange)
![License](https://img.shields.io/badge/
---

# 📖 Overview

This project implements a fully local and offline Retrieval-Augmented Generation (RAG) architecture capable of processing enterprise documentation and answering natural language questions without exposing corporate data to external APIs.

The solution combines:

- Semantic Search
- Vector Databases
- Local Embeddings
- Quantized LLM Inference
- Enterprise Document Processing
- CPU-Only Deployment

This architecture is designed for corporate environments where:

- Sensitive data cannot leave the organization
- Internet access is restricted
- OpenAI API usage is not allowed
- Low infrastructure cost is required
- Full observability and control are desired

---

# 🎯 Business Problem

Organizations accumulate large volumes of unstructured knowledge:

- Procedures
- Operational manuals
- Technical documentation
- Internal policies
- Knowledge bases
- Excel reports
- Process documentation

Finding information manually is slow, error-prone and difficult to scale.

This project transforms static documentation into an intelligent knowledge retrieval platform capable of answering questions grounded in corporate data.

---

# 🏗 High-Level Architecture

```text
                        ┌────────────────────┐
                        │ Enterprise Docs    │
                        │ PDF DOCX XLSX TXT  │
                        └─────────┬──────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │ Document Extraction Layer│
                    └─────────┬────────────────┘
                              │
                              ▼
                    ┌──────────────────────────┐
                    │ Chunking Engine          │
                    │ 500 chars + overlap 100  │
                    └─────────┬────────────────┘
                              │
                              ▼
                    ┌──────────────────────────┐
                    │ Embeddings               │
                    │ MiniLM-L6-v2            │
                    └─────────┬────────────────┘
                              │
                              ▼
                    ┌──────────────────────────┐
                    │ FAISS Vector Store       │
                    └─────────┬────────────────┘
                              │
                    User Query
                              │
                              ▼
                    ┌──────────────────────────┐
                    │ Semantic Retrieval       │
                    │ Top-K Similar Chunks     │
                    └─────────┬────────────────┘
                              │
                              ▼
                    ┌──────────────────────────┐
                    │ Prompt Construction      │
                    └─────────┬────────────────┘
                              │
                              ▼
                    ┌──────────────────────────┐
                    │ Local LLM (GGUF)         │
                    │ Qwen 2.5 Instruct        │
                    └─────────┬────────────────┘
                              │
                              ▼
                           Answer
```

---

# 🛠 Technical Stack

## Backend

- Python 3.11+
- Llama.cpp
- llama-cpp-python

## Vector Search

- FAISS

## Embeddings

- sentence-transformers
- all-MiniLM-L6-v2

## Document Processing

- PyPDF
- python-docx
- pandas
- openpyxl

## User Interface

- Streamlit (optional)

## Models

Default:

```text
Qwen2.5-1.5B-Instruct-Q4_K_M.gguf
```

Alternative:

```text
Phi-3 Mini
Gemma 3 1B
Mistral 7B
Llama 3.2
```

---

# 📂 Repository Structure

```text
RAG/
│
├── app.py
├── ingest.py
├── query.py
│
├── docs/
│   ├── policy.pdf
│   ├── manual.docx
│   └── report.xlsx
│
├── models/
│   └── Qwen2.5-1.5B-Instruct-Q4_K_M.gguf
│
├── vector_db/
│   ├── base.index
│   └── chunks.pkl
│
├── requirements.txt
│
└── README.md
```

---

# 🔎 How It Works

## Step 1 - Document Ingestion

Documents are loaded from the local repository.

Supported formats:

```text
PDF
DOCX
XLSX
TXT
```

---

## Step 2 - Chunking

Large documents are split into smaller semantic chunks.

Configuration:

```python
chunk_size = 500
chunk_overlap = 100
```

Benefits:

- Better retrieval quality
- Lower context pollution
- Reduced hallucinations

---

## Step 3 - Embedding Generation

Chunks are transformed into vector representations.

Model:

```text
all-MiniLM-L6-v2
```

Vector dimension:

```text
384
```

---

## Step 4 - Vector Database

Each embedding is stored inside FAISS.

Advantages:

✅ Fast

✅ Lightweight

✅ Offline

✅ Production-proven

✅ Low memory consumption

---

## Step 5 - Retrieval

User question:

```text
"What is the SLA for critical incidents?"
```

is transformed into an embedding.

FAISS locates the most semantically related chunks.

Example:

```text
Top 5 Chunks
```

---

## Step 6 - Context Grounding

Retrieved chunks are injected into the prompt.

Example:

```text
Context:
...
...
...

Question:
What is the SLA?

Answer:
```

This significantly reduces hallucination rates.

---

## Step 7 - Local Inference

Prompt is processed using:

```text
Qwen2.5-1.5B-Instruct
```

through:

```text
llama.cpp
```

No internet access required.

No external API calls required.

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/your-user/local-rag.git

cd local-rag
```

---

## Create Virtual Environment

### Windows

```powershell
python -m venv rag_env

rag_env\Scripts\activate
```

### Linux

```bash
python -m venv rag_env

source rag_env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📥 Download LLM

Place the GGUF model inside:

```text
models/
```

Example:

```text
Qwen2.5-1.5B-Instruct-Q4_K_M.gguf
```

---

# 📄 Add Documents

Place files inside:

```text
docs/
```

Example:

```text
docs/

incident_sla.pdf

operational_manual.pdf

corporate_policy.docx

knowledge_base.xlsx
```

---

# 🔨 Build Vector Database

Run:

```bash
python ingest.py
```

Output:

```text
vector_db/

base.index

chunks.pkl
```

---

# 💬 Run Chat

```bash
python app.py
```

Example:

```text
Question:
What is the incident escalation process?

Answer:
According to the operational procedure...
```

---

# 📊 Performance

Benchmark Environment:

```text
Windows 11
Intel i7
16GB RAM
CPU Only
```

| Metric | Result |
|----------|----------|
| Embedding Generation | ~10k chunks/min |
| Retrieval Latency | <50ms |
| Inference Time | 1-5 seconds |
| RAM Usage | 2-4GB |
| GPU Required | No |

---

# 🔒 Security

This architecture was designed following enterprise security principles.

## Data Residency

All data remains on-premises.

```text
Documents never leave the machine.
```

---

## API Independence

No dependency on:

```text
OpenAI
Anthropic
Google
Azure
AWS
```

---

## Privacy

Suitable for:

- Internal procedures
- Corporate documentation
- Restricted reports
- Operational knowledge bases
- Confidential records

---

# 📈 Scalability Considerations

Current architecture:

```text
Single Node
```

Can evolve to:

```text
Multi-Tenant RAG
```

using:

- ChromaDB
- Pinecone
- Milvus
- Weaviate

---

# 🧠 Design Decisions

## Why FAISS?

Chosen because:

- Mature ecosystem
- Extremely fast similarity search
- Offline-first
- Low operational complexity

---

## Why MiniLM?

Chosen because:

- Excellent latency
- Low resource consumption
- Strong semantic search quality

---

## Why Qwen 2.5?

Compared against:

- Gemma 270M
- TinyLlama
- Phi Mini

Qwen demonstrated significantly better:

- Retrieval grounding
- Instruction following
- Enterprise document QA

while still running comfortably on CPU.

---

# ✅ Strengths

- Fully Offline
- CPU Only
- Reproducible
- Enterprise Friendly
- Low Cost
- Vendor Independent

---

# 🚧 Roadmap

## Retrieval

- [ ] BM25 Hybrid Search
- [ ] Metadata Filtering
- [ ] Semantic Cache

## Generation

- [ ] Streaming Tokens
- [ ] Conversation History
- [ ] Multi-Query Retrieval

## Enterprise

- [ ] SharePoint Integration
- [ ] Teams Knowledge Bot
- [ ] Outlook Integration
- [ ] Azure AD Authentication

## AI Enhancements

- [ ] BGE Reranker
- [ ] LangGraph Agents
- [ ] Knowledge Graph Layer
- [ ] Tool Calling

---

# 📚 Engineering Principles

This project follows:

## Architecture

- Clean Architecture
- Separation of Concerns
- Modular Design

## Software Engineering

- SOLID Principles
- Reusability
- Maintainability

## AI Engineering

- Retrieval Augmented Generation
- Context Grounding
- Hallucination Reduction
- Efficient Local Inference

---

# 👩‍💻 Author

## Sabrina Goes Paixão Barga Santos

**Backend Engineer | Data Engineer | AI Engineer**

### Expertise

- Artificial Intelligence
- Retrieval Augmented Generation (RAG)
- Generative AI
- Data Engineering
- Machine Learning
- Python
- SQL
- FastAPI
- Enterprise Automation
- Microsoft Ecosystem

### Technical Interests

- LLM Applications
- AI Agents
- Knowledge Systems
- MLOps
- Data Platforms
- Enterprise Architecture

---

# ⭐ Support

If you found this project useful:

- Star the repository
- Open an issue
- Submit improvements
- Share feedback

Contributions are welcome.

---

## License

MIT License
