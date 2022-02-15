from managers.class_utils.validator.validator import Validator
from functions.utils.util import (get_operator)

class IfCompareV2(Validator):
    """Class to add a condition in the validators"""
    def __init__(self, comparation, validators=[]):
        self.comparation = comparation
        self.validators = validators
        self.parent_data = {}
        self.parent_key_error = ''

    def validate(self, data, vars_):
        if self.comparation[0].__class__.__name__ == 'FieldV2':
            value_1 = self.comparation[0].get_value(data, self.parent_data)
        else:
            value_1 = self.comparation[0]
        if self.comparation[2].__class__.__name__ == 'FieldV2':
            value_2 = self.comparation[2].get_value(data, self.parent_data)
        else:
            value_2 = self.comparation[2]
        if self.comparation[1] == 'in':
            value_to_compare = value_1 in value_2
        elif self.comparation[1] == 'not in':
            value_to_compare = value_1 not in value_2
        else:
            operator = get_operator(self.comparation[1])
            value_to_compare = operator(value_1, value_2)
        if value_to_compare:
            for validator in self.validators:
                validator.parent_data = self.parent_data
                validator.parent_key_error = self.parent_key_error
                validator.list_data = self.list_data
                validator.validate(data, vars_)
