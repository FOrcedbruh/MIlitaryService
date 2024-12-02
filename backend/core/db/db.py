from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from ..settings import settings
from typing import AsyncGenerator

class DB():
    def __init__(
            self,
            db_url: str = settings.dbcfg.url,
            pool_size: int = settings.dbcfg.pool_size,
            echo: bool = settings.dbcfg.echo
        ):

        self.engine = create_async_engine(
            echo=echo,
            pool_size=pool_size,
            url=db_url
        )
        self.session_generation: AsyncGenerator[AsyncSession, None] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommi=False,
            expire_on_commit=False
        )
    async def generate_session(self) -> AsyncSession:
        async with self.generate_session as session:
            yield session

db = DB()