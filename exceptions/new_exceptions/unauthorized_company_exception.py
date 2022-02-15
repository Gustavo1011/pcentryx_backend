"""Excepción para usuario no autorizado en una compañía"""
from exceptions.new_exception import NewException


class UnauthorizedCompanyException(NewException):
    """Excepción para usuario no autorizado en una compañía"""
    def __init__(self, field_error):
        super().__init__()
        self.field_error = field_error

    def get_data(self):
        return {
            'type': 'DevelopmentException',
            'errors': [{
                'field_error': self.field_error,
                'code_error': 'ERROR-XXXXXXX',
                'description': 'El usuario actual no está autorizado para la compañía'
            }]
        }
