# Pydantic it’s a Python library that validates and structures data.
from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    API_PREFIX: str = "/api"

    DEBUG: bool = False

    DATABASE_URL: str = ""

    ALLOWED_ORIGINS: str = ""

    OPENAI_API_KEY: str = ""

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []

    # Config is a Pydantic hook that lets settings know how to behave.
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
