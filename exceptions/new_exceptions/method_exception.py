"""Excepción para campo repetido en una lista de diccionarios"""
from exceptions.new_exception import NewException

class MethodException(NewException):
    """Excepción para valores repetidos en lista de diccionarios"""
    def __init__(
        self, key_error, description_error=None,
        code_error='ERROR-0000104', type_exception='DevelopmentException'
    ):
        super().__init__()
        self.key_error = key_error
        self.code_error = code_error
        self.type_exception = type_exception
        if description_error is None:
            self.description_error = 'La función del objeto retorna un valor inválido'
        else:
            self.description_error = description_error

    def get_data(self):
        return {
            'type': self.type_exception,
            'errors': [{
                'field_error': self.key_error,
                'code_error': self.code_error,
                'description': self.description_error
            }]
        }
