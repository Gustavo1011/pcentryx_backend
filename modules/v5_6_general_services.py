"""
v5_6_general_services.py: General_services module
"""
from flask_jwt_extended import jwt_required
from functions.utils.request_type import get_data
from apis.v5_6_general_services.get_type_computers.module import GetTypeComputersModule

def get_type_computers(**kwargs):
    """Function for get type computers"""
    module = GetTypeComputersModule(get_data())
    return module.use_api()
