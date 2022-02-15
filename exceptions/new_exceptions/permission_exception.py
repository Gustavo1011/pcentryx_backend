'''Excepción para campo repetido'''
from exceptions.new_exception import NewException

class PermissionException(NewException):
    '''Excepción para campo repetido'''
    def __init__(self):
        super().__init__()

    def get_data(self):
        return {
            'type': 'DevelopmentException',
            'errors': [{
                'field_error': None,
                'code_error': 'ERROR-0000100',
                'description': 'El usuario de la sesión no presenta los permisos necesarios'
            }]
        }
