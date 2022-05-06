""" Define la respuesta del API get_type_computers """
from managers.class_utils.response.response_api import ResponseAPI
from managers.class_utils.response.model_fields import ModelFields

class GetTypeComputersResponse(ResponseAPI):
    """ Clase para definir la salida del API get_type_computers """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.model_name = "TypeComputer"

    def set_response(self):
        """ Función que define la salida del API """
        self.set_structure([
            ModelFields()
        ])
