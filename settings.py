import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PORT: int = int(os.getenv("PORT", 8000))
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017/tour_agency")
    TOURS_COLLECTION: str = "tours"

settings = Settings()
