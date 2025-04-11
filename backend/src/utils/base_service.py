from abc import ABC


class BaseApiService(ABC):
    base_url: str = ...