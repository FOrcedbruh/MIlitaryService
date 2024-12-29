from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
BASE_URL: str = os.environ.get("BASE_URL")
CHAT_ID: str = os.environ.get("CHAT_ID")


class Settings(BaseSettings):
    token: str = BOT_TOKEN
    base_url: str = BASE_URL
    chat_id: str = CHAT_ID


settings = Settings()