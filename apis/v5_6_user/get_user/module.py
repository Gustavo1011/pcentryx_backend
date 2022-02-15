""" Define el módulo del API get_user """
from apis.v5_6_user.get_user.input import GetUserInput
from apis.v5_6_user.get_user.validator import GetUserValidator
from apis.v5_6_user.get_user.flow import GetUserFlow
from apis.v5_6_user.get_user.response import GetUserResponse
from managers.class_utils.module.module_api import ModuleAPI

class GetUserModule(ModuleAPI):
    """ Clase para definir el módulo del API get_user """
    def __init__(self, data):
        """ Constructor de la clase """
        super().__init__()
        self.data = data
        self.input_api = GetUserInput()
        self.validator_api = GetUserValidator()
        self.flow_api = GetUserFlow()
        self.response_api = GetUserResponse()
