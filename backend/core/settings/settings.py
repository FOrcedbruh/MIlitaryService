from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL: str = os.environ.get("DB_URL")
PORT: str = os.environ.get("PORT")


class RunConfig(BaseModel):
    port: int = int(PORT),
    reload: bool = True



class DBConfig(BaseModel):
    url: str = DB_URL,
    pool_size: int = 50
    echo: bool = True



class Settings(BaseSettings):
    runcfg: RunConfig = RunConfig()
    dbcfg: DBConfig = DBConfig()



settings = Settings()