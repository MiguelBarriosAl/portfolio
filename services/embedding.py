from typing import List

from langchain_community.embeddings import OllamaEmbeddings


class EmbeddingService:
    def __init__(self, model: str = "nomic-embed-text"):
        self.model_name = model
        self.client = OllamaEmbeddings(model=self.model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.client.embed_documents(texts)

    def embed_query(self, query: str) -> List[float]:
        return self.client.embed_query(query)
