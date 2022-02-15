"""
users.py: File for the user module
"""
from flask_injector import inject
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_babel import gettext
from interfaces.users.manage_users import IManageUsers
from rules.request.user import rules
from libraries.validator import Validator
from libraries.response import request_response

@inject
def search(data_provider: IManageUsers) -> list:
    """Returns a list of filtered users"""
    return data_provider.search()

@jwt_required
@inject
def post(data_provider: IManageUsers):
    """Create a new user"""
    validator = Validator(rules["store"])
    validate = validator.validate(request.json)
    if not validate:
        return request_response(validator.errors.items())
    user = request.json
    return data_provider.store(user)

@jwt_required
@inject
def get(data_provider: IManageUsers, user_id):
    """Get information from a specific user"""
    if not str(user_id).isdigit():
        return jsonify({"msg": gettext("ID must only contain an integer")}), 400
    return data_provider.get(user_id)

@jwt_required
@inject
def put(data_provider: IManageUsers, user_id):
    """Update a specific user"""
    if not str(user_id).isdigit():
        return jsonify({"msg": gettext("ID must only contain an integer")}), 400

    validator = Validator(rules["update"])
    validate = validator.validate(request.json)
    if not validate:
        return request_response(validator.errors.items())
    user = request.json
    return data_provider.update(user_id, user)

@jwt_required
@inject
def delete(data_provider: IManageUsers, user_id):
    """Delete a specific user"""
    if not str(user_id).isdigit():
        return jsonify({"msg": gettext("ID must only contain an integer")}), 400
    return data_provider.delete(user_id)
