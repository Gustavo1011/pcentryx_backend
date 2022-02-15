from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.invalid_attr_value_exception import InvalidAttrValueException
from functions.utils.util import get_operator


class ValidatorAttrValue(Validator):
    """Class for validator Attribute Value"""
    def __init__(self, name_var):
        self.name_var = name_var
        self.filters = []
        self.value = None
        self.index = 0
        self.field_error = 'unknown'
        self.description = None

    def validate(self, data, vars_):
        if self.value is None:
            raise Exception('No se envía el value')
        if self.is_invalid(data, vars_):
            raise InvalidAttrValueException(self.field_error, self.description, self.index)

    def is_invalid(self, data, vars_):
        """Verifica si existen datos inválidos según la lógica de negocio"""
        registry = vars_[self.name_var]
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

    def filter(self, filters=[]):
        self.filters = filters
        return self

    def by_field(self, field_name):
        self.field_error = field_name
        return self

    def describe(self, description):
        self.description = description
        return self
