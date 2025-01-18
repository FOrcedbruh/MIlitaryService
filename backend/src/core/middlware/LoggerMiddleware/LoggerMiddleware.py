import logging
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LoggingMiddlaware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        logger.info(f"Запрос: {request.method} {request.url}")

        response = await call_next(request)

        logger.info(f"Ответ: статус {response.status_code} для {request.method} {request.url}")

        return response
