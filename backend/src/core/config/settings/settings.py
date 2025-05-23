from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL: str = os.environ.get("DB_URL")
PORT: int = os.environ.get("PORT")
S3_URL: str = os.environ.get("S3_URL")
AWS_ACCESS_KEY: str = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY: str = os.environ.get("AWS_SECRET_KEY")
AWS_BUCKETNAME: str = os.environ.get("AWS_BUCKETNAME")
GET_S3_URL: str = os.environ.get("GET_S3_URL")
BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
CHAT_ID: int = os.environ.get("CHAT_ID")
DADATA_BASE_URL: str = os.environ.get("DADATA_BASE_URL")


class RunConfig(BaseModel):
    port: int = PORT
    reload: bool = True

class BotConfig(BaseModel):
    token: str = BOT_TOKEN
    chat_id: int = CHAT_ID

class DBConfig(BaseModel):
    url: str = DB_URL
    pool_size: int = 50
    echo: bool = True

class S3Config(BaseModel):
    url: str = S3_URL
    secret_key: str = AWS_SECRET_KEY
    access_key: str = AWS_ACCESS_KEY
    bucketname: str = AWS_BUCKETNAME
    get_url: str = GET_S3_URL
    len_get_s3_url: int = len(GET_S3_URL)

class DadataConfig(BaseModel):
    base_url: str = DADATA_BASE_URL


class Settings(BaseSettings):
    runcfg: RunConfig = RunConfig()
    dbcfg: DBConfig = DBConfig()
    s3cfg: S3Config = S3Config()
    botCfg: BotConfig = BotConfig()
    dadatacfg: DadataConfig = DadataConfig()



settings = Settings()