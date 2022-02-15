from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.method_exception import MethodException
from functions.utils.util import get_model

class ValidatorMethodV2(Validator):
    """Class to validate the result of a method of a model"""
    def __init__(
            self, registry_name, method_name, value,
            args=[],
            key_error='unknown', description_error=None,
            code_error='ERROR-0000104',
            type_exception='DevelopmentException',
            dynamic_error=False
        ):
        self.registry_name = registry_name
        self.method_name = method_name
        self.value = value
        self.key_error = key_error
        self.parent_data = {}
        self.parent_key_error = ''
        self.description_error = description_error
        self.code_error = code_error
        self.type_exception = type_exception
        self.args = args
        self.list_data = []
        self.dynamic_error = dynamic_error

    def validate(self, data, vars_):
        if self.is_correct(data, vars_) is False:
            if self.key_error is None:
                total_key_error = None
            else:
                total_key_error = self.parent_key_error + self.key_error
            raise MethodException(
                key_error=total_key_error,
                description_error=self.description_error,
                code_error=self.code_error,
                type_exception=self.type_exception
            )

    def is_correct(self, data, vars):
        new_args = []
        for method_arg in self.args:
            if method_arg.__class__.__name__ == 'FieldV2':
                method_arg.list_data = self.list_data
                new_args.append(method_arg.get_value(data, self.parent_data))
            else:
                new_args.append(method_arg)
        if self.registry_name in self.parent_data:
            registry = self.parent_data.get(self.registry_name)
        else:
            registry = data.get(self.registry_name)
        if hasattr(registry, self.method_name) is False:
            raise Exception('El registro no tiene ese mÃ©todo')
        function = getattr(registry, self.method_name)
        if self.value.__class__.__name__ == 'FieldV2':
            value_to_compare = self.parent_data.get(self.value.name)
        else:
            value_to_compare = self.value
        if self.dynamic_error is True:
            result = function(*new_args)
            if 'key_error' in result:
                self.key_error = result.get('key_error')
            return function(*new_args).get('value') == value_to_compare
        return function(*new_args) == value_to_compare
