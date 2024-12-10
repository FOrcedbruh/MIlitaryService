from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


BOT_TOKEN: str = os.environ.get("BOT_TOKEN")


class Settings(BaseSettings):
    token: str = BOT_TOKEN



settings = Settings()