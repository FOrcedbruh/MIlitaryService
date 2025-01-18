from ...base.exceptions import BaseException
from .exc_details import PRODUCT_NOT_FOUND_EXCEPTION_STATUS, PRODUCT_NOT_FOUND_EXCEPTION_DETAIL


class NotFoundProductException(BaseException):
    status: int = PRODUCT_NOT_FOUND_EXCEPTION_STATUS
    detail: str = PRODUCT_NOT_FOUND_EXCEPTION_DETAIL

    def __init__(self):
        super().__init__(status=self.status, detail=self.detail)