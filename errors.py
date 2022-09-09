from support.imports import *

from app import app


class BasicException(Exception):
    status_code = 0
    default_message = 'Unknown Error'

    async def __init__(self, message: str = None, status_code: int = None):
        super().__init__(message)
        self.message = message
        request.status = self.status_code
        if status_code is not None:
            self.status_code = status_code

    async def to_dict(self):
        return {
            'message': self.message or self.default_message
        }


class NotFound(BasicException):
    status_code = 404
    default_message = 'NOT_FOUND'


class AuthError(BasicException):
    status_code = 401
    default_message = 'UNAUTHORIZED'


class BadRequest(BasicException):
    status_code = 400
    default_message = 'BAD_REQUEST'
