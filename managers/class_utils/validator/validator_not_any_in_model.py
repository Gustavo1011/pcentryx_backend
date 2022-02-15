from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.invalid_attr_in_registry_exception import InvalidAttrInRegistryException
from functions.utils.util import get_model, get_operator

class ValidatorNotAnyInModel(Validator):
    """Class for validator if not exist any registries of model with any attributes"""
    def __init__(self, model_name):
        self.model = get_model(model_name)
        self.filters = []
        self.field_error = 'unknown'
        self.description = None

    def validate(self, data, vars_):
        if self.is_invalid(data, vars_):
            raise InvalidAttrInRegistryException(self.field_error, self.description)

    def is_invalid(self, data, vars_):
        """Verifica si existen datos inválidos según la lógica de negocio"""
        filters = []
        for filter_ in self.filters:
            if isinstance(filter_[2], str) and filter_[2][0] == '#':
                filter_[2] = self.get_vars_of_locate(vars_, filter_[2][1:])
            elif isinstance(filter_[2], bool):
                filter_[2] = str(filter_[2]).lower()
            operator = get_operator(filter_[1])
            filters.append(operator(getattr(self.model, filter_[0]), filter_[2]))
        return self.model.query.filter(
            *filters
        ).count() > 0

    def filter(self, filters=[]):
        self.filters = filters
        return self

    def by_field(self, field_name):
        self.field_error = field_name
        return self

    def describe(self, description):
        self.description = description
        return self

    def get_vars_of_locate(self, vars_, locate):
        parts = locate.split('.')
        return getattr(vars_[parts[0]], parts[1])

