'''Excepción para campo repetido'''
from exceptions.new_exception import NewException


class InvalidAttrValueException(NewException):
    '''Excepción para atributo invalido de un valor'''
    def __init__(self, field='unknown', description=None, index=0):
        super().__init__()
        self.field = field
        if description is not None:
            self.description = description
        else:
            self.description = 'value has invalid attributes'
        self.index = index

    def get_data(self):
        return {
            'type': 'DevelopmentException',
            'errors': [{
                'field_error': '{}.{}'.format(self.field, self.index),
                'code_error': 'ERROR-0000013',
                'description': self.description
            }]
        }