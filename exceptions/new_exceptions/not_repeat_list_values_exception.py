'''Excepción para campo repetido'''
from exceptions.new_exception import NewException

class NotRepeatListValuesException(NewException):
    '''Excepción para valores repetidos en lista'''
    def __init__(self, field, index):
        super().__init__()
        self.field = field
        self.index = index

    def get_data(self):
        return {
            'type': 'CustomerException',
            'errors': [{
                'field_error': '{}.{}'.format(self.field, self.index),
                'code_error': 'ERROR-0000119',
                'description': 'Repeated values ​​in list'
            }]
        }
