from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from ..settings import settings
from typing import AsyncGenerator

class DB():
    def __init__(
            self,
            db_url: str,
            pool_size: int,
            echo: bool
        ):

        self.engine = create_async_engine(
            url=db_url,
            echo=echo,
            pool_size=pool_size
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


db = DB(db_url=settings.dbcfg.url, pool_size=settings.dbcfg.pool_size, echo=settings.dbcfg.echo)