from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    database_url: str = Field(
        validation_alias="DATABASE_URL",         # alias typo
    )
    log_level: str = "INFO"
    parse_schedule_minutes: int = 5

    postgres_user: str 
    postgres_password: str
    postgres_db: str

    api_url: str


settings = Settings()
