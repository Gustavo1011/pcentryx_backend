""" Define el flujo para el API get_session """
from flask_jwt_extended import get_jwt_identity
from models.user import User

class GetSessionFlow:
    """ Clase para definir el flujo del API get_session """
    def __init__(self):
        """ Constructor de la clase """
        self.data = None

    def action(self):
        """ Función que define el flujo del API """
        current_user = get_jwt_identity()
        user = User.query.filter(
            User.deleted == 'false',
            User.id ==  current_user.get('id')
        ).first()

        return user
