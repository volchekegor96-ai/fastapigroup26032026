from pydantic_settings import BaseSettings, SettingsConfigDict
from pymongo.asynchronous import settings


class Settings(BaseSettings):
    URL: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )



settings = Settings()