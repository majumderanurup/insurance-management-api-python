from app.exceptions.base import AppException


class ProductBusinessRuleException(AppException):
    status_code = 400

    def __init__(self, message: str):
        super().__init__(message)