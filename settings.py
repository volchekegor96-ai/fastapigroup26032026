import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PORT: int = int(os.getenv("PORT", 8000))
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017/tour_agency")
    TOURS_COLLECTION: str = "tours"

settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    URI: str
    SHOP_NAME_DB: str = 'shop_project'
    BOOKS_COLLECTION: str = 'books'
    SHOP_NAME_DB: str = 'shop22'
    BOOKS_COLLECTION: str = 'books222'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


settings = Settings()
