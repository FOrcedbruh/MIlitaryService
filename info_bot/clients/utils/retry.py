from time import sleep
from core import logger

class MaxRetriesException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def retry(times: int = 5, sleep_secs: int = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts <= times:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    logger.error(f"Попытка получить ответ от сервиса провалена: {error}")
                    sleep(sleep_secs)
                    if attempts >= times:
                        logger.error(f"Сервис не дал ответа")
                        raise MaxRetriesException("Max retries exceeded")
                    attempts += 1
                    
        return wrapper
    return decorator