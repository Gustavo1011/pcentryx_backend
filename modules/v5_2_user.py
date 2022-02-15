"""
v5_2_user.py: User module
"""
from flask_jwt_extended import jwt_required
from functions.utils.request_type import get_data
from apis.v5_2_user.get_user.module import GetUserModule

# pylint: disable=unused-argument
@jwt_required
def get_user(**kwargs):
    """Function for get user"""
    module = GetUserModule(get_data())
    return module.use_api()
