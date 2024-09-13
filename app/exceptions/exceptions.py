from .base import BaseSanicException

class ValidationError(BaseSanicException):
    def __init__(self, message, status_code = 400) -> None:
        super().__init__(message, status_code)