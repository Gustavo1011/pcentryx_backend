"""Clase padre para las validaciones"""

from exceptions.handlers.simple_handler import SimpleHandler
from exceptions.handlers.handler_by_frontend import HandlerByFrontend
from exceptions.new_exception import NewException
from managers.class_utils.validator.validator_input import ValidatorInput


class ValidatorAPI:
    """Clase padre para las validaciones"""

    def __init__(self):
        self.module = None
        self.validators = []
        self.response_error = None
        self.response_object = {}
        self.data = []
        self.vars = {}

    def validate_api(self):
        return None

    def set_validators(self, validators):
        self.validators.extend(validators)

    def validate(self):
        """Valida información"""
        self.validate_api()
        self.validators.insert(0, ValidatorInput(self.module))
        try:
            for validator in self.validators:
                validator.parent_data = self.module.data
                validator.list_data = [{}, self.module.data]
                validator.validate(self.module.data, self.vars)
        except NewException as exception:
            parts_version = self.module.input_api.version[1:].split('.')
            if int(parts_version[0]) > 5 or (int(parts_version[0]) == 5 and int(parts_version[1]) > 0):
                handler = HandlerByFrontend()
            else:
                handler = SimpleHandler()
            self.response_error = handler.handle_exception(exception)

    def has_response_error(self):
        """Verifica si existe respuesta de error"""
        return self.response_error is not None
