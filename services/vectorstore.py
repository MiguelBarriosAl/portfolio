from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from config import settings
from services.embedding import EmbeddingService


class QdrantVectorStore:
    def __init__(self, collection_name: str = settings.collection_name):
        self.client = QdrantClient(url=settings.qdrant_url)
        self.embedding_service = EmbeddingService()
        self.collection_name = collection_name

        # Crear la colección si no existe
        if not self.client.collection_exists(self.collection_name):
            self.client.recreate_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=768, distance=Distance.COSINE
                ),  # 768 para nomic
            )

    def index_documents(self, texts: list[str], metadatas: list[dict] = None):
        vectors = self.embedding_service.embed_documents(texts)

        payloads = [
            {**(meta or {}), "page_content": text}
            for text, meta in zip(texts, metadatas or [{} for _ in texts])
        ]

        points = [
            PointStruct(id=str(uuid4()), vector=vector, payload=meta)
            for vector, meta in zip(vectors, payloads)
        ]

        self.client.upsert(collection_name=self.collection_name, points=points)


_vectorstore = None


def get_vectorstore() -> QdrantVectorStore:
    global _vectorstore
    if _vectorstore is None:
        _vectorstore = QdrantVectorStore()
    return _vectorstore
