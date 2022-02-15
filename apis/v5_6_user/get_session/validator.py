""" Define las validaciones del API get_session """
from managers.class_utils.validator.validator_api import ValidatorAPI
from managers.class_utils.validator.validator_boolean import ValidatorBoolean
from flask_jwt_extended import get_jwt_identity
from models.user import User

class GetSessionValidator(ValidatorAPI):
    """ Clase para definir las validaciones del API get_session """
    def __init__(self):
        """ Constructor de la clase """
        super().__init__()

    def validate_api(self):
        """ Función que define las validaciones del API """
        current_user = get_jwt_identity()
        user = User.query.filter(
            User.deleted == 'false',
            User.id ==  current_user.get('id')
        ).first()

        self.set_validators([
            ValidatorBoolean(user.deleted is False).describe(
                'El usuario de la sesion debe ser no eliminado'
            ).set_code_error('ERROR-00088').by_field(
                'user_id'
            ).set_type_exception('DevelopmentException')
        ])
