""" Define la respuesta del API get_user """
from managers.class_utils.response.response_api import ResponseAPI
from managers.class_utils.response.model_fields import ModelFields
from managers.class_utils.response.model_field import ModelField

class GetUserResponse(ResponseAPI):
    """ Clase para definir la salida del API get_user """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()
        self.model_name = "User"

    def set_response(self):
        """ Función que define la salida del API """
        self.set_structure([
            ModelField('id'),
            ModelField('core_id'),
            ModelField('name'),
            ModelField('lastname'),
            ModelField('username'),
            ModelField('email'),
            ModelField('avatar_url'),
            ModelField('is_enabled')
        ])
