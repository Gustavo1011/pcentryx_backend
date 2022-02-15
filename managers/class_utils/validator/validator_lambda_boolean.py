from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.boolean_exception import BooleanException


class ValidatorLambdaBoolean(Validator):
    """Class for validator boolean"""
    def __init__(self, lambda_function, data, default=False):
        self.lambda_function = lambda_function
        self.data = data
        self.default = default
        self.field_error = 'unknown'
        self.description = None,
        self.code_error = 'ERROR-XXXXXXX'
        self.type_exception = 'DevelopmentException'

    def validate(self, data, vars_):
        if self.lambda_function(self.data) is self.default:
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
