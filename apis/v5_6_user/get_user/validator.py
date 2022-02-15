""" Define las validaciones del API get_user """
from managers.class_utils.validator.validator_api import ValidatorAPI
from managers.class_utils.validator.validator_exist import ValidatorExist
from flask_jwt_extended import get_jwt_identity

class GetUserValidator(ValidatorAPI):
    """ Clase para definir las validaciones del API get_user """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()

    def validate_api(self):
        """ Función que define las validaciones del API """

        self.set_validators([
            ValidatorExist('User', 'id', 'user_id')
            ])
