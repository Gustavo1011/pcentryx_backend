from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.invalid_attr_in_registry_exception import InvalidAttrInRegistryException
from functions.utils.util import get_operator

class ValidatorAttrInModel(Validator):
    """Class for validator if model has any attributes with any values"""
    def __init__(self, locate):
        self.locate = self.get_locate(locate)
        self.filters = []
        self.field_error = 'unknown'
        self.description = None

    def validate(self, data, vars_):
        if self.is_invalid(data, vars_):
            raise InvalidAttrInRegistryException(self.field_error, self.description)

    def is_invalid(self, data, vars_):
        """Verifica si existen datos inválidos según la lógica de negocio"""
        registry = vars_[self.locate]
        for filter_ in self.filters:
            if filter_[1] == 'in':
                if getattr(registry, filter_[0]) not in filter_[2]:
                    return True
            elif filter_[1] == 'not in':
                if getattr(registry, filter_[0]) in filter_[2]:
                    return True
            else:
                operator = get_operator(filter_[1])
                if operator(getattr(registry, filter_[0]), filter_[2]) is False:
                    return True
        return False

    def get_locate(self, locate):
        if isinstance(locate, str) is False:
            raise Exception('Debe ser una cadena')
        if locate[0] != '#':
            raise Exception('Debe tener # al comienzo')
        return locate[1:]

    def filter(self, filters=[]):
        self.filters = filters
        return self

    def by_field(self, field_name):
        self.field_error = field_name
        return self

    def describe(self, description):
        self.description = description
        return self

