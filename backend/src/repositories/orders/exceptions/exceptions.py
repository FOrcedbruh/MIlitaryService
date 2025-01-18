from ...base.exceptions import BaseException
from .exc_details import NOT_FOUND_ORDER_EXCEPTION_DETAIL, NOT_FOUND_ORDER_EXCEPTION_STATUS


class NotFoundOrderException(BaseException):
    status: int = NOT_FOUND_ORDER_EXCEPTION_STATUS
    detail: str = NOT_FOUND_ORDER_EXCEPTION_DETAIL

    def __init__(self):
        super().__init__(status=self.status, detail=self.detail)

