from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.boolean_exception import BooleanException


class ValidatorBoolean(Validator):
    """Class for validator boolean"""
    def __init__(self, value, default=False):
        self.value = value
        self.default = default
        self.field_error = 'unknown'
        self.description = None,
        self.code_error = 'ERROR-XXXXXXX'
        self.type_exception = 'DevelopmentException'

    def validate(self, data, vars_):
        if self.value is self.default:
            raise BooleanException(
                self.field_error, self.code_error,
                self.description, self.type_exception
            )

    def by_field(self, field_name):
        self.field_error = field_name
        return self

    def describe(self, description):
        self.description = description
        return self

    def set_code_error(self, code_error):
        self.code_error = code_error
        return self

    def set_type_exception(self, type_exception):
        self.type_exception = type_exception
        return self
