"""Excepción para campo repetido en una lista de diccionarios"""
from exceptions.new_exception import NewException

class NotRepeatInListDictException(NewException):
    """Excepción para valores repetidos en lista de diccionarios"""
    def __init__(self, field, index):
        super().__init__()
        self.field = field
        self.index = index

    def get_data(self):
        return {
            'type': 'CustomerException',
            'errors': [{
                'field_error': '{}.{}'.format(
                    self.field, self.index
                ),
                'code_error': 'ERROR-0000101',
                'description': 'Valores repetidos en una lista de diccionarios'
            }]
        }
