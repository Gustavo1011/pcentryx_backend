""" Define el módulo del API get_type_computers """
from apis.v5_6_general_services.get_type_computers.input import GetTypeComputersInput
from apis.v5_6_general_services.get_type_computers.validator import GetTypeComputersValidator
from apis.v5_6_general_services.get_type_computers.flow import GetTypeComputersFlow
from apis.v5_6_general_services.get_type_computers.response import GetTypeComputersResponse
from managers.class_utils.module.module_api import ModuleAPI

class GetTypeComputersModule(ModuleAPI):
    """ Clase para definir el módulo del API get_type_computers """
    def __init__(self, data):
        """ Constructor de la clase """
        super().__init__()
        self.data = data
        self.input_api = GetTypeComputersInput()
        self.validator_api = GetTypeComputersValidator()
        self.flow_api = GetTypeComputersFlow()
        self.response_api = GetTypeComputersResponse()
