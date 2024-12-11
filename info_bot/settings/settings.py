from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
BASE_URL: str = os.environ.get("BASE_URL")


class Settings(BaseSettings):
    token: str = BOT_TOKEN
    base_url: str = BASE_URL


settings = Settings()