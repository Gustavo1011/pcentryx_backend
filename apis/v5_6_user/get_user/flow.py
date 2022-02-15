""" Define el flujo para el API get_user """
from models.user import User

class GetUserFlow:
    """ Clase para definir el flujo del API get_user """
    def __init__(self):
        """ Constructor de la clase """
        self.data = None

    def action(self):
        """ Función que define el flujo del API """
        
        user = User.query.filter(
            ~User.id.in_([1, 2]),
            User.id == self.data.get('user_id'),
            User.deleted == "false"
        ).first()

        return user
