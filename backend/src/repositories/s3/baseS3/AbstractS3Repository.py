from abc import ABC, abstractmethod



class AbstractS3Repository(ABC):

    @abstractmethod
    async def get_client(self): ...
    
    @abstractmethod
    async def upload_file(self, file): ... 

    @abstractmethod
    async def delete_file(self, key: str): ...