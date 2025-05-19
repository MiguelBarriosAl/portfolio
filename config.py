from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    QDRANT_URL: str = "http://localhost:6333"
    COLLECTION_NAME: str = "portfolio"

    model_config = SettingsConfigDict(env_file=".env.dev", env_file_encoding="utf-8")

settings = Settings()
