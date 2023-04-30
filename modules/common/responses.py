from typing import Any

from flask import jsonify


def response_items(status_code: int, items: list):
    payload = {
        "data": {
            "items": [jsonify(item) for item in items],
            "total": len(items)
        }
    }
    item_response = jsonify(payload)
    item_response.status_code = status_code
    return item_response


def response_entity(status_code: int, data: Any):
    json_object = jsonify(data)
    payload = {
        "data": json_object
    }
    item_response = jsonify(payload)
    item_response.status_code = status_code
    return item_response


def response_message(status_code: int, message: str):
    payload = {
        "data": {
            "code": str(status_code),
            "message": message
        }
    }
    item_response = jsonify(payload)
    item_response.status_code = status_code
    return item_response


def ok(message):
    return response_message(200, message)


def created(message):
    return response_message(201, message)


def bad_request(message):
    return response_message(400, message)


def not_found(message):
    return response_message(404, message)


def conflict(message):
    return response_message(409, message)


def unprocessable_entity(message):
    return response_message(422, message)


def internal_server_error(message):
    return response_message(500, message)
