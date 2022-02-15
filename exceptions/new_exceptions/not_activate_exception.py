'''Excepción para campo is_enabled'''
from flask_babel import gettext

from exceptions.new_exception import NewException
from libraries.response import entity_response


class NotActivateException(NewException):
    '''Excepción para campo repetido'''
    def __init__(self, field):
        super().__init__()
        self.field = field

    def get_data(self):
        return {
            'type': 'DevelopmentException',
            'errors': [{
                'field_error': self.field,
                'code_error': 'ERROR-00000059',
                'description': 'The model must be activated'
            }]
        }