'''Excepción para campo repetido'''
from exceptions.new_exception import NewException

class NotExistListValuesException(NewException):
    '''Excepción para valores no existentes en lista'''
    def __init__(self, field, index):
        super().__init__()
        self.field = field
        self.index = index

    def get_data(self):
        return {
            'type': 'CustomerException',
            'errors': [{
                'field_error': '{}.{}'.format(self.field, self.index),
                'code_error': 'ERROR-0000011',
                'description': 'The model related to the field of the list does not exist'
            }]
        }
