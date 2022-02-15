'''Excepción para campo repetido'''
from exceptions.new_exception import NewException


class NotExistValueException(NewException):
    '''Excepción para campo repetido'''
    def __init__(self, field, index):
        super().__init__()
        self.field = field
        self.index = index

    def get_data(self):
        return {
            'type': 'DevelopmentException',
            'errors': [{
                'field_error': '{}.{}'.format(self.field, self.index),
                'code_error': 'ERROR-0000012',
                'description': 'The model related to the value does not exist'
            }]
        }