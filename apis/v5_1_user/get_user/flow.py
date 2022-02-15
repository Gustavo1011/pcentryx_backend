""" Define el flujo para el API get_user """
from models.user import User

class GetUserFlow:
    """ Clase para definir el flujo del API get_user """
    def __init__(self):
        """ Constructor de la clase """
        self.data = None

    def action(self):
        """ Función que define el flujo del API """
        return User.query.filter_by(
            id=self.data.get('user_id')
        ).first()
