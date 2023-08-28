# framework/http/response.py

from json import dumps


def as_json(message):
    return dumps({
        'message': message
    })