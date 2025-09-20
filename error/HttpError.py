import logging as log
from http import HTTPStatus

from fastapi import HTTPException

class NotFoundError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code= HTTPStatus.NOT_FOUND, detail= message)
        log.error(message)

class ValidationError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code= HTTPStatus.BAD_REQUEST, detail=message)
        log.error(message)

class UnauthorizedError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code= HTTPStatus.UNAUTHORIZED, detail=message)