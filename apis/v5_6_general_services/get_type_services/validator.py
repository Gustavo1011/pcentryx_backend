""" Define las validaciones del API get_type_services """
from managers.class_utils.validator.validator_api import ValidatorAPI

class GetTypeServicesValidator(ValidatorAPI):
    """ Clase para definir las validaciones del API get_type_services """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()

    def validate_api(self):
        """ Función que define las validaciones del API """
        self.set_validators([])
