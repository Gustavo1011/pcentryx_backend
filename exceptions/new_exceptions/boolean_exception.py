'''Excepción para campo repetido'''
from exceptions.new_exception import NewException


class BooleanException(NewException):
    '''Excepción para atributo invalido de un valor'''
    def __init__(self, field_error, code_error, description, type_exception='DevelopmentException'):
        super().__init__()
        self.field_error = field_error
        self.code_error = code_error
        self.description = description
        self.type_exception = type_exception

    def get_data(self):
        return {
            'type': self.type_exception,
            'errors': [{
                'field_error': self.field_error,
                'code_error': self.code_error,
                'description': self.description
            }]
        }