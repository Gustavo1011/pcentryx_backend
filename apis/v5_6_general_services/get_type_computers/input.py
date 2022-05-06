""" Define las entradas del API get_type_computers """
from managers.class_utils.input.input_api import InputAPI

class GetTypeComputersInput(InputAPI):
    """ Clase para definir las entradas del API get_type_computers """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.module_name = "general_services"
        self.tag = "GeneralServices Management"
        self.api_name = "get_type_computers"
        self.version = "v5.6"
        self.route = "apis/type_computers/all"
        self.type_request = "GET"
        self.type_response = "200"
        self.description = "Obtener todos los tipos de computadora"

    def set_inputs(self):
        """ Función que define las entradas del API """
        self.set_path([])
        self.set_query([])
        self.set_body([])
