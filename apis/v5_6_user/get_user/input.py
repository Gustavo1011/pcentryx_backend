""" Define las entradas del API get_user """
from managers.class_utils.input.input_api import InputAPI
from managers.class_utils.input.input_integer import InputInteger

class GetUserInput(InputAPI):
    """ Clase para definir las entradas del API get_user """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.module_name = "user"
        self.tag = "User Management"
        self.api_name = "get_user"
        self.version = "v5.6"
        self.route = "apis/users/{user_id}"
        self.type_request = "GET"
        self.type_response = "200"
        self.description = "Obtener información de un usuario en específico"

    def set_inputs(self):
        """ Función que define las entradas del API """
        self.set_path([InputInteger('user_id')])
        self.set_query([])
        self.set_body([])
