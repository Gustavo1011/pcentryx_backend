"""Excepción para registro no existente y no habilitado"""
from flask_babel import gettext

from exceptions.new_exception import NewException
from libraries.response import entity_response


class NotEnabledExistException(NewException):
    """Excepción para registro existente y no habilitado"""
    def __init__(self, field):
        super().__init__()
        self.field = field

    def get_data(self):
        return {
            'type': 'DevelopmentException',
            'errors': [{
                'field_error': self.field,
                'code_error': 'ERROR-XXXXXXX',
                'description': 'The model related to the field is not enabled'
            }]
        }

    def get_response(self):
        """Obtener respuesta de la excepción"""
        return entity_response(
            400,
            errors=[{
                'field': self.field,
                'message': gettext(self.message),
                'extra': self.extra
            }]
        )