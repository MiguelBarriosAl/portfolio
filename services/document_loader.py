from pathlib import Path
from typing import List

from langchain_community.document_loaders import TextLoader, UnstructuredPDFLoader
from langchain_core.documents import Document
from pdfminer.high_level import extract_text


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


def load_pdf_or_txt(file_path: str) -> list[Document]:
    path = Path(file_path)
    if path.suffix == ".pdf":
        text = extract_text(file_path)
    elif path.suffix == ".txt":
        text = path.read_text(encoding="utf-8")
    else:
        raise ValueError("Unsupported file type")

    return [Document(page_content=text, metadata={"source": str(path.name)})]
