from typing import Dict

from marshmallow import ValidationError
from werkzeug.exceptions import InternalServerError


class HexagonalError:
    status_code: int
    data: Dict

    def __init__(self, status_code: int = 400, data: Dict = None):
        self.data = data if data else dict()
        self.status_code = status_code

    def to_dict(self):
        return dict(
            data=self.data,
            status_code=self.status_code,
            message='Unexpected Error'
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
