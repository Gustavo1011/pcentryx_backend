'''Excepción para campo repetido'''
from exceptions.new_exception import NewException

class InvalidAttrInRegistryException(NewException):
    '''Excepción para cuando un registro tiene atributos inválidos'''
    def __init__(self, field='unknown', description=None):
        super().__init__()
        self.field = field
        if description is not None:
            self.description = description
        else:
            self.description = 'The registry has invalid attributes'

    def get_data(self):
        return {
            'type': 'DevelopmentException',
            'errors': [{
                'field_error': self.field,
                'code_error': 'ERROR-0000006',
                'description': self.description
            }]
        }
