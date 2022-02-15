from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.not_repeat_list_values_exception import NotRepeatListValuesException


class ValidatorNotRepeatListValues(Validator):
    """Class for validator Exist"""
    def __init__(self, field_name):
        self.field_name = field_name
        self.parts = []
        self.index = None

    def validate(self, data, vars):
        value = data.get(self.field_name)
        if value is not None and self.check_is_repeat(value) is True:
            raise NotRepeatListValuesException(self.field_name, self.index)

    def check_is_repeat(self, values):
        """Verifica si se repiten los valores en una lista"""
        elements = []
        for value in values:
            if value in elements:
                self.index = len(elements)
                return True
            elements.append(value)
        return False
