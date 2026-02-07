from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Netriex AIOps Copilot"
    APP_ENV: str = "dev"
    DEBUG: bool = True

    JWT_PRIVATE_KEY: str
    JWT_PUBLIC_KEY: str

    DATABASE_URL: str
    REDIS_URL: str

    AWS_REGION: str

    class Config:
        env_file = ".env"

settings = Settings()
