""" Define el módulo del API get_session """
from apis.v5_6_user.get_session.input import GetSessionInput
from apis.v5_6_user.get_session.validator import GetSessionValidator
from apis.v5_6_user.get_session.flow import GetSessionFlow
from apis.v5_6_user.get_session.response import GetSessionResponse
from managers.class_utils.module.module_api import ModuleAPI

class GetSessionModule(ModuleAPI):
    """ Clase para definir el módulo del API get_session """
    def __init__(self, data):
        """ Constructor de la clase """
        super().__init__()
        self.data = data
        self.input_api = GetSessionInput()
        self.validator_api = GetSessionValidator()
        self.flow_api = GetSessionFlow()
        self.response_api = GetSessionResponse()
