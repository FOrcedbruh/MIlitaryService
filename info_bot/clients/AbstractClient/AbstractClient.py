from abc import ABC, abstractmethod


class AbstractClient(ABC):

    @abstractmethod
    async def get_all(self) -> list: ...

    @abstractmethod
    async def get_one(self): ...