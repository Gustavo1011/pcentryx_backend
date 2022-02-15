from managers.class_utils.validator.validator import Validator


class ValidatorListValues(Validator):
    """Class for validator List Values"""
    def __init__(self, name_var):
        self.name_var = name_var
        self.validators = []

    def validate(self, data, vars_):
        for index, value in enumerate(data[self.name_var]):
            for validator in self.validators:
                validator.value = value
                validator.index = index
                validator.attr_error = self.name_var
                validator.validate(data, vars_)

    def validate_each_one(self, validators=[]):
        self.validators = validators
        return self
