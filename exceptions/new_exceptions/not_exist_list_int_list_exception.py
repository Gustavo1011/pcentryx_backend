"""Excepción para valor en lista que no existe en otra lista"""
from exceptions.new_exception import NewException


class NotExistListInListException(NewException):
    """Excepción para valores no existentes en lista"""
    def __init__(self, field, index, code_error, type_exception, description):
        super().__init__()
        self.field = field
        self.index = index
        self.code_error = code_error
        self.type_exception = type_exception
        self.description = description

    def get_data(self):
        return {
            'type': self.type_exception,
            'errors': [{
                'field_error': '{}.{}'.format(self.field, self.index),
                'code_error': self.code_error,
                'description': self.description
            }]
        }
