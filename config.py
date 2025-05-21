from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    qdrant_url: str
    collection_name: str = "portfolio"
    model_name: str = "nomic-embed-text"
    upload_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
