import random
import ujson
from sanic.response import json
from app.constants.constants import HTTPStatusCodes


def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

def json_file_to_dict(_file: str) -> dict:
    """
    convert json file data to dict

    :param str _file: file location including name

    :rtype: dict
    :return: converted json to dict
    """
    config = None
    try:
        with open(_file) as config_file:
            config = ujson.load(config_file)
    except (TypeError, FileNotFoundError, ValueError) as exception:
        print(exception)

    return config

def send_response(data=None, status_code=HTTPStatusCodes.SUCCESS.value, meta=None, body: dict = None, headers=None, purge_response_keys=False):
    """
    :param data: final response data
    :param status_code: success status code, default is 200
    :param body: Optional: Response body dict in v4 format.
    :param headers: Optional : Response headers to be sent to clients.
    :param purge_response_keys: Optional : Converts response into dict
    :return {'is_success': True, 'data': data, 'status_code': status_code}
    :param meta results
    """
    if body is not None:
        return json(body=body, status=body["status_code"])
    data = {"data": data, "is_success": True, "status_code": status_code}
    if meta:
        data["meta"] = meta
    if purge_response_keys:
        return data
    return json(body=data, status=status_code, headers=headers)