""" Define las validaciones del API get_user """
from managers.class_utils.validator.validator_api import ValidatorAPI
from managers.class_utils.validator.validator_exist import ValidatorExist

class GetUserValidator(ValidatorAPI):
    """ Clase para definir las validaciones del API get_user """

    def validate_api(self):
        """ Función que define las validaciones del API """
        self.set_validators([
            ValidatorExist('User', 'id', 'user_id')
        ])
