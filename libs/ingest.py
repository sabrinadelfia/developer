import os
import pickle
import faiss
import numpy as np
import pandas as pd

from pypdf import PdfReader
from docx import Document

from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

DOCS_FOLDER = "docs"
VECTOR_FOLDER = "vector_db"

embedder = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def read_pdf(filepath):

    text = ""

    reader = PdfReader(filepath)

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def read_docx(filepath):

    doc = Document(filepath)

    return "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )


def read_excel(filepath):

    df = pd.read_excel(
        filepath,
        engine="openpyxl"
    )

    return "\n".join(
        df.astype(str)
        .agg(" | ".join, axis=1)
        .tolist()
    )


def load_documents():

    documents = []

    for file in os.listdir(DOCS_FOLDER):

        path = os.path.join(
            DOCS_FOLDER,
            file
        )

        try:

            if file.lower().endswith(".pdf"):

                documents.append(
                    read_pdf(path)
                )

            elif file.lower().endswith(".docx"):

                documents.append(
                    read_docx(path)
                )

            elif file.lower().endswith(".xlsx"):

                documents.append(
                    read_excel(path)
                )

        except Exception as ex:

            print(
                f"Erro: {file} -> {ex}"
            )

    return documents


def create_vector_database():

    documents = load_documents()

    text = "\n".join(
        documents
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(
        text
    )

    embeddings = embedder.encode(
        chunks,
        show_progress_bar=True
    )

    embeddings = np.array(
        embeddings
    ).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    os.makedirs(
        VECTOR_FOLDER,
        exist_ok=True
    )

    faiss.write_index(
        index,
        os.path.join(
            VECTOR_FOLDER,
            "base.index"
        )
    )

    with open(
        os.path.join(
            VECTOR_FOLDER,
            "chunks.pkl"
        ),
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )

    print(
        "Base vetorial criada."
    )


if __name__ == "__main__":

    create_vector_database()