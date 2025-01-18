from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import AsyncGenerator

class DatabaseConnection():
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
            autocommit=False,
            expire_on_commit=False
        )
    async def generate_session(self) -> AsyncSession:
        async with self.session_generation() as session:
            yield session