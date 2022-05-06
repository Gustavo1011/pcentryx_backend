""" Define el módulo del API get_type_services """
from apis.v5_6_general_services.get_type_services.input import GetTypeServicesInput
from apis.v5_6_general_services.get_type_services.validator import GetTypeServicesValidator
from apis.v5_6_general_services.get_type_services.flow import GetTypeServicesFlow
from apis.v5_6_general_services.get_type_services.response import GetTypeServicesResponse
from managers.class_utils.module.module_api import ModuleAPI

class GetTypeServicesModule(ModuleAPI):
    """ Clase para definir el módulo del API get_type_services """
    def __init__(self, data):
        """ Constructor de la clase """
        super().__init__()
        self.data = data
        self.input_api = GetTypeServicesInput()
        self.validator_api = GetTypeServicesValidator()
        self.flow_api = GetTypeServicesFlow()
        self.response_api = GetTypeServicesResponse()
