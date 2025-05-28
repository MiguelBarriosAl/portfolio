from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    qdrant_url: str
    collection_name: str = "portfolio"
    openai_api_key: str
    request_timeout: int = 60
    openai_embedding_model: str = "text-embedding-3-small"
    openai_llm_model: str = "gpt-3.5-turbo"
    max_tokens: int = 500
    upload_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
