from pathlib import Path
from typing import List

import nltk
from langchain.schema import Document
from langchain_community.document_loaders import TextLoader, UnstructuredPDFLoader

for resource in ["punkt", "averaged_perceptron_tagger"]:
    try:
        nltk.data.find(
            f"tokenizers/{resource}" if resource == "punkt" else f"taggers/{resource}"
        )
    except LookupError:
        nltk.download(resource)


def load_documents(path: str) -> List[Document]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix == ".pdf":
        loader = UnstructuredPDFLoader(file_path.as_posix(), strategy="auto")
    elif file_path.suffix in [".txt", ".md"]:
        loader = TextLoader(file_path.as_posix(), encoding="utf-8")
    else:
        raise ValueError("Unsupported file type")

    return loader.load()
