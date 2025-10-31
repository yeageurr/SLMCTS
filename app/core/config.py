from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "Loan Management System"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = "sqlite:///./loan_management.db"
    # For PostgreSQL: postgresql://user:password@localhost/dbname
    # For MySQL: mysql+pymysql://user:password@localhost/dbname
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # OTP
    OTP_EXPIRE_MINUTES: int = 10
    OTP_LENGTH: int = 6
    
    # Email (configure based on your email provider)
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: Optional[int] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: Optional[str] = None
    
    # SMS (configure based on your SMS provider)
    SMS_API_KEY: Optional[str] = None
    SMS_API_URL: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()