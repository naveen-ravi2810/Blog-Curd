from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    db_uri: str = os.environ.get("db_uri")
    test_db_uri: str = os.environ.get("test_db_uri")

settings=Settings()
