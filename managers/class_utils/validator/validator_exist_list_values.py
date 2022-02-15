from libraries.utils import snake_case
from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.not_exist_list_values_exception import NotExistListValuesException
from functions.utils.util import get_model


class ValidatorExistListValues(Validator):
    """Class for validator Exist in list of values"""
    def __init__(self, model, field_model, field_data, has_filter_deleted=False):
        self.model = get_model(model)
        self.field_model = field_model
        self.field_data = field_data
        self.filters = []
        if has_filter_deleted is False:
            self.filters.append(getattr(self.model, 'deleted') == "False")
        self.field_error = field_data
        self.description = None
        self.index = None

    def validate(self, data, vars_):
        if self.not_exist(data):
            raise NotExistListValuesException(self.field_data, self.index)
        if hasattr(self, 'query'):
            vars_[snake_case(self.model.__name__)] = self.query.first()

    def not_exist(self, data):
        """Verifica si existe ID"""
        for index, value in enumerate(data.get(self.field_data, []) or []):
            self.query = self.model.query.filter(
                getattr(self.model, self.field_model) == value,
                *self.filters
            )
            if self.query.count() == 0:
                self.index = index
                return True
        return False
