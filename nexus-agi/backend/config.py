from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    app_name: str = 'NEXUS-AGI'
    environment: str = Field(default='development')
    debug: bool = False

    api_host: str = '0.0.0.0'
    api_port: int = 8000

    postgres_dsn: str = 'postgresql+psycopg://postgres:postgres@postgres:5432/nexus'
    redis_url: str = 'redis://redis:6379/0'
    qdrant_url: str = 'http://qdrant:6333'
    neo4j_url: str = 'bolt://neo4j:7687'
    neo4j_user: str = 'neo4j'
    neo4j_password: str = 'password'

    jwt_secret: str = 'change-me'
    jwt_algorithm: str = 'HS256'
    access_token_minutes: int = 30
    refresh_token_days: int = 30

    encryption_key: str = 'change-with-fernet-key'

    llm_provider: str = 'openai'
    openai_api_key: str = ''

    celery_broker_url: str = 'redis://redis:6379/1'
    celery_result_backend: str = 'redis://redis:6379/2'


@lru_cache
def get_settings() -> Settings:
    return Settings()
