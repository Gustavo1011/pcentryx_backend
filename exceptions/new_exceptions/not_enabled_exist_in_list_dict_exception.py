"""Excepción para registro no existente no habilitado"""
from exceptions.new_exception import NewException

class NotEnabledExistInListDictException(NewException):
    """EExcepción para registro no existente no habilitado"""
    def __init__(self, field, index, name_value):
        super().__init__()
        self.field = field
        self.index = index
        self.name_value = name_value

    def get_data(self):
        return {
            'type': 'CustomerException',
            'errors': [{
                'field_error': '{}.{}.{}'.format(
                    self.field, self.index, self.name_value
                ),
                'code_error': 'ERROR-0000110',
                'description': 'Valor no habilitado no existente'
            }]
        }
