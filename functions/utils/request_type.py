""" request_type.py: Obtiene el metodo del request """
from flask import request


def get_data():
    """ Obtiene el metodo del request """
    data = {}
    if request.args:
        data = request.args
    if request.view_args:
        data = {**data, **request.view_args}
    if request.method == 'POST' or request.method == 'PUT' and request.json is not None:
        data = {**data, **request.json}
    return data
