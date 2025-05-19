import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter

from services.document_loader import load_documents
from services.vectorstore import QdrantVectorStore


def main():
    parser = argparse.ArgumentParser(description="Indexar documentos en Qdrant")
    parser.add_argument(
        "--file", required=True, help="Ruta al archivo PDF o TXT a indexar"
    )
    args = parser.parse_args()

    file_path = Path(args.file)

    if not file_path.exists():
        raise FileNotFoundError(f"❌ Archivo no encontrado: {file_path}")

    # 1. Cargar documento
    documents = load_documents(str(file_path))

    # 2. Dividir en chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    split_docs = splitter.split_documents(documents)

    # 3. Extraer texto plano y metadatos
    texts = [doc.page_content for doc in split_docs]
    metadatas = [doc.metadata for doc in split_docs]

    # 4. Indexar en Qdrant
    store = QdrantVectorStore()
    store.index_documents(texts, metadatas)

    print(f"✅ {len(texts)} chunks indexados correctamente desde {file_path}")


if __name__ == "__main__":
    main()
