from typing import List

from langchain_openai import OpenAIEmbeddings


class EmbeddingService:
    def __init__(self, model: str = "text-embedding-3-small"):
        self.model_name = model
        self.client = OpenAIEmbeddings(model=self.model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.client.embed_documents(texts)

    def embed_query(self, query: str) -> List[float]:
        return self.client.embed_query(query)
