"""Config"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Global Settings"""
    APP_NAME: str = "Research API"
    MONGODB_URL: str = ""
    REDIS_URL: str = ""
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    TOKEN_ISSUER: str = "https://auth.racenginee.com"

    class Config:
        """Env source"""
        env_file = ".env"


settings = Settings()
