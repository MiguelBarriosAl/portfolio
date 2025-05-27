from typing import List

from langchain_openai import OpenAIEmbeddings

from config import settings


class EmbeddingService:
    def __init__(self):
        self.client = OpenAIEmbeddings(
            model=settings.openai_embedding_model,
            openai_api_key=settings.openai_api_key,
        )

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.client.embed_documents(texts)

    def embed_query(self, query: str) -> List[float]:
        return self.client.embed_query(query)
