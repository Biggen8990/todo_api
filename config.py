import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_LIFETIME_MINUTES = int(os.getenv("JWT_LIFETIME_MINUTES", 60))
    DATABASE_URL = os.getenv("DATABASE_URL")


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = Config.DATABASE_URL or "sqlite:///dev.db"


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = Config.DATABASE_URL


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = Config.DATABASE_URL
