'''Excepción para estructura de diccionario'''
from exceptions.new_exception import NewException
import re

class StructureException(NewException):
    '''Clase para excepción de estructura'''
    def __init__(self, value):
        super().__init__()
        self.value = value

    def get_data(self):
        errors = []
        for key, values in self.value.items():
            for value in values:
                if isinstance(value, str):
                    errors.append({
                        'field_error': key,
                        'code_error': self.get_code(value),
                        'description': value
                    })
                elif isinstance(value, dict):
                    value_key = list(value.keys())[0]
                    value_value = list(value.values())[0][0]
                    errors.append({
                        'field_error': '{}.{}{}'.format(key, value_key, self.get_key(value_value)),
                        'code_error': self.get_code(value_value),
                        'description': self.get_description(value_value)
                    })
        return {
            'type': 'CustomerException',
            'errors': errors
        }

    def get_code(self, value_description):
        description = value_description
        if isinstance(description, dict):
            description = list(description.values())[0][0]
        if isinstance(description, dict):
            description = list(description.values())[0][0]
        if re.match(r"Valor no permitido .*", description):
            return 'ERROR-0000001'
        elif re.match(r"El valor máximo es .*", description):
            return 'ERROR-0000002'
        elif re.match(r"El valor mínimo es .*", description):
            return 'ERROR-0000003'
        elif re.match(r"Formato de valor no válido", description):
            return 'ERROR-0000004'
        elif re.match(r"Campo requerido", description):
            return 'ERROR-0000007'
        elif re.match(r"La longitud máxima es .*", description):
            return 'ERROR-0000008'
        elif re.match(r"La longitud mínima es .*", description):
            return 'ERROR-0000009'
        return 'ERROR-XXXXXXX'

    def get_description(self, value_description):
        description = value_description
        if isinstance(description, dict):
            description = list(description.values())[0][0]
        if isinstance(description, dict):
            description = list(description.values())[0][0]
        return description

    def get_key(self, value):
        if isinstance(value, dict):
            new_value = list(value.keys())[0]
            if isinstance(new_value, dict):
                return '.{}'.format(self.get_key(new_value))
            return '.{}'.format(new_value)
        return ''
