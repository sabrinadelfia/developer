import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from llama_cpp import Llama

VECTOR_FOLDER = "vector_db"

MODEL_PATH = r"models/Qwen2.5-1.5B-Instruct-Q4_K_M.gguf"

TOP_K = 5

embedder = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=8192,
    n_threads=8,
    verbose=False
)

index = faiss.read_index(
    f"{VECTOR_FOLDER}/base.index"
)

with open(
    f"{VECTOR_FOLDER}/chunks.pkl",
    "rb"
) as f:

    chunks = pickle.load(f)


def consultar(pergunta):

    query_embedding = embedder.encode(
        [pergunta]
    )

    D, I = index.search(
        np.array(
            query_embedding
        ).astype("float32"),
        TOP_K
    )

    contexto = "\n\n".join(
        [
            chunks[idx]
            for idx in I[0]
        ]
    )

    prompt = f"""
Você é um assistente corporativo.

Responda somente usando
o contexto abaixo.

Se não souber, responda:

"Não encontrei essa informação."

CONTEXTO:

{contexto}

PERGUNTA:

{pergunta}

RESPOSTA:
"""

    resposta = llm(
        prompt,
        max_tokens=500,
        temperature=0.2
    )

    return resposta[
        "choices"
    ][0][
        "text"
    ].strip()