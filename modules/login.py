"""
login.py: File for the login module
"""
from flask import request
from flask_injector import inject
from interfaces.users.user_access import IUserAccess
from rules.request.user import rules
from libraries.validator import Validator
from libraries.response import request_response

@inject
def post(data_provider: IUserAccess):
    """Log in"""
    timezone = request.headers.get('timezone', 'UTC')
    validator = Validator(rules["login"])
    validate = validator.validate({
        **request.json,
        'timezone': timezone
    })
    if not validate:
        return request_response(validator.errors.items())
    return data_provider.login(request, timezone)
