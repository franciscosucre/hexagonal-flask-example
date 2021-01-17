from typing import Dict, Optional

from marshmallow import ValidationError


class HexagonalError(Exception):
    status_code: int
    data: Dict

    def __init__(self, code: str, message: Optional[str] = None, status_code: int = 400, data: Optional[Dict] = None):
        self.data = data if data else dict()
        self.status_code = status_code
        self.message = message if message else 'An Error has ocurred'
        self.code = code


def hexagonal_error_handler(error: HexagonalError):
    return dict(
        data=error.data,
        status_code=error.status_code,
        message=error.message,
        code=error.code
    )


def marshmallow_error_handler(error: ValidationError):
    return dict(
        data=dict(
            input=error.data,
            valid_data=error.valid_data,
            errors=error.normalized_messages()
        ),
        status_code=422,
        message='Unexpected Error'
    )


def internal_server_error_handler(error):
    return dict(
        status_code=500,
        message='Unexpected Error'
    )
