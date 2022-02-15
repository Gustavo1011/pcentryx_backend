'''Validador de campo único'''
from libraries.validator import Validator
from exceptions.new_exceptions.unique_exception import UniqueException
from functions.general.general import accent
from managers.utils.manager_general import unaccent
from functions.utils.util import (
    get_model, remove_extra_spaces, get_operator
)

class ValidatorUnique(Validator):
    '''Clase para validar campo único'''
    def __init__(self, model, field_model, field_data, filters=[]):
        self.model = get_model(model)
        self.field_model = field_model
        self.field_data = field_data
        self.deleted = []
        self.filters = filters
        self.filter_keys = []
        for filter_ in self.filters:
            self.filter_keys.append(filter_[0])

    def validate(self, data, vars):
        '''Valida la data'''
        if self.is_repeated(data):
            raise UniqueException(self.field_data, self.filter_keys)

    def is_repeated(self, data):
        '''Verifica si se repite un campo'''
        value = remove_extra_spaces(data[self.field_data])
        filters = []
        for filter_ in self.filters:
            operator = get_operator(filter_[1])
            filters.append(operator(getattr(self.model, filter_[0]), filter_[2]))
        return self.model.query.filter(
            unaccent(getattr(self.model, self.field_model)).ilike('{}'.format(accent(value))),
            *self.deleted,
            *filters
        ).count() > 0
