'''Excepción para campo repetido'''
from flask_babel import gettext

from exceptions.new_exception import NewException
from libraries.response import entity_response


class NotExistException(NewException):
    '''Excepción para campo repetido'''
    def __init__(self, field, filters=[]):
        super().__init__()
        self.field = field
        self.filters = filters

    def get_data(self):
        description = 'El registro no existe'
        if len(self.filters) > 0:
            description += ' por los campos ' + ', '.join(self.filters)
        return {
            'type': 'DevelopmentException',
            'errors': [{
                'field_error': self.field,
                'code_error': 'ERROR-0000005',
                'description': description
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
            }],
            message="Invalid request"
        )