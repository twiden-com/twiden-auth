from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    supabase_service_key: str
    environment: str = "dev"
    port: int = 8000
    log_level: str = 'info'
    model_config = {"env_file": ".env"}

settings = Settings()
