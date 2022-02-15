from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.not_activate_exception import NotActivateException
from functions.utils.util import get_model, snake_case


class ValidatorEnabledDirect(Validator):
    """Class for validator Exist"""
    def __init__(self, model, field_model, field_data, data_direct=None):
        self.model = get_model(model)
        self.field_model = field_model
        self.field_data = field_data
        self.data_direct = data_direct
        self.deleted = [getattr(self.model, 'deleted') == "False"]
        self.query = None

    def validate(self, data, vars_):
        if self.not_exist(data) is not None:
            data_model = self.not_exist(data)
            if data_model.is_enabled is False:
                raise NotActivateException(self.field_data)
            
    def not_exist(self, data):
        """Verifica si existe ID"""
        value = data[self.field_data]
        if self.data_direct is  not None:
            value = self.data_direct

        self.query = self.model.query.filter(
            getattr(self.model, self.field_model) == value,
            *self.deleted
        )
        return self.query.first()