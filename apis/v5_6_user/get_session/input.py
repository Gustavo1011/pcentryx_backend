""" Define las entradas del API get_session """
from managers.class_utils.input.input_api import InputAPI

class GetSessionInput(InputAPI):
    """ Clase para definir las entradas del API get_session """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.module_name = "user"
        self.tag = "User Management"
        self.api_name = "get_session"
        self.version = "v5.6"
        self.route = "apis/users/get_session"
        self.type_request = "GET"
        self.type_response = "200"
        self.description = " Obtener información de la sesión"

    def set_inputs(self):
        """ Función que define las entradas del API """
        self.set_path([])
        self.set_query([])
        self.set_body([])
