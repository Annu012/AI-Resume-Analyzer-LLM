# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Resume Analyzer"
    ENV: str = "development"

    class Config:
        env_file = ".env"

# Define settings at the module level
settings = Settings()
