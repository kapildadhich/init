from app.constants.constants import HTTPStatusCodes
from sanic.response import json

from sanic.response import json

def format_error_response(message, status_code):
    response = {
        "data": {
            "error": {
                "message": message
            }
        },
        "is_success": True,
        "status_code": status_code
    }
    return json(response, status=status_code)

async def handle_exception(request, exception):
    status_code = getattr(exception, 'status_code', 500)
    return format_error_response(str(exception), status_code)


class BaseSanicException(Exception):
    def __init__(
        self,
        error,
        status_code= HTTPStatusCodes.BAD_REQUEST.value
    ):
        self._error = error
        self._status_code = status_code