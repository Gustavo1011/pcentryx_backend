'''Excepción para campo repetido'''
from exceptions.new_exception import NewException

class UniqueException(NewException):
    '''Excepción para campo repetido'''
    def __init__(self, field, filters=[]):
        super().__init__()
        self.field = field
        self.filters = filters

    def get_data(self):
        description = 'El campo es repetido'
        if len(self.filters) > 0:
            description += ' por los campos ' + ', '.join(self.filters)
        return {
            'type': 'CustomerException',
            'errors': [{
                'field_error': self.field,
                'code_error': 'ERROR-0000102',
                'description': description
            }]
        }
