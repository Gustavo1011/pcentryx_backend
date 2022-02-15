""" Define la respuesta del API get_session """
from managers.class_utils.response.response_api import ResponseAPI
from managers.class_utils.response.model_fields import ModelFields
from managers.class_utils.response.method_value import MethodValue
from managers.class_utils.response.model_field import ModelField

class GetSessionResponse(ResponseAPI):
    """ Clase para definir la salida del API get_session """
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
            ModelField('is_enabled'),
            MethodValue('get_permissions', 'permissions'),
            MethodValue('get_current_session', 'session'),
            MethodValue('get_origin_company', 'company_principal')
        ])
