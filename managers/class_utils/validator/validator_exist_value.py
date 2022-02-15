from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.not_exist_value_exception import NotExistValueException
from functions.utils.util import get_model, snake_case


class ValidatorExistValue(Validator):
    """Class for validator Exist Value"""
    def __init__(self, model):
        self.model = get_model(model)
        self.value = None
        self.query = None
        self.index = 0
        self.attr_error = 'Unknown'

    def validate(self, data, vars_):
        if self.value is None:
            raise Exception('No se envía el value')
        if self.not_exist(data):
            raise NotExistValueException(self.attr_error, self.index)
        vars_[snake_case(self.model.__name__)] = self.query.first()

    def not_exist(self, data):
        """Verifica si existe ID"""
        self.query = self.model.query.filter(
            getattr(self.model, 'id') == self.value,
            getattr(self.model, 'deleted') == "false"
        )
        return self.query.count() == 0
