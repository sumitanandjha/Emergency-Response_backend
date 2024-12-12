from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./emergency.db"
    API_KEY: str = "your_api_key"
    SMS_GATEWAY_URL: str = "https://sms.example.com/send"
    EMAIL_SERVER: str = "smtp.example.com"

    class Config:
        env_file = ".env"

settings = Settings()
