
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from uuid import uuid4
from services.embedding import EmbeddingService
from config import settings


class QdrantVectorStore:
    def __init__(self, collection_name: str = settings.COLLECTION_NAME):
        self.client = QdrantClient(url=settings.QDRANT_URL)
        self.embedding_service = EmbeddingService()
        self.collection_name = collection_name

        # Crear la colección si no existe
        if not self.client.collection_exists(self.collection_name):
            self.client.recreate_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE)  # 768 para nomic
            )

    def index_documents(self, texts: list[str], metadatas: list[dict] = None):
        vectors = self.embedding_service.embed_documents(texts)

        payload = metadatas if metadatas else [{} for _ in texts]

        points = [
            PointStruct(id=str(uuid4()), vector=vector, payload=meta)
            for vector, meta in zip(vectors, payload)
        ]

        self.client.upsert(collection_name=self.collection_name, points=points)
