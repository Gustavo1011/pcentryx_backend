"""Excepción para una actualizacion con menos de un archivo"""
from exceptions.new_exception import NewException


class NotAtLeastOneFileException(NewException):
    """Excepción para una actualizacion con menos de un archivo"""
    def __init__(self, field, code_error, type_exception, description):
        super().__init__()
        self.field = field
        self.code_error = code_error
        self.type_exception = type_exception
        self.description = description

    def get_data(self):
        return {
            'type': self.type_exception,
            'errors': [{
                'field_error': self.field,
                'code_error': self.code_error,
                'description': self.description
            }]
        }
