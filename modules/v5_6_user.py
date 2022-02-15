"""
v5_6_user.py: User module
"""
from flask_jwt_extended import jwt_required
from functions.utils.request_type import get_data
from apis.v5_6_user.get_user.module import GetUserModule
from apis.v5_6_user.get_session.module import GetSessionModule

@jwt_required
def get_user(**kwargs):
    """Function for get user"""
    module = GetUserModule(get_data())
    return module.use_api()

@jwt_required
def get_session(**kwargs):
    """Function for get session"""
    module = GetSessionModule(get_data())
    return module.use_api()
