""" Define el flujo para el API get_type_services """
from models.type_service import TypeService

class GetTypeServicesFlow:
    """ Clase para definir el flujo del API get_type_services """
    def __init__(self):
        """ Constructor de la clase """
        self.data = None

    def action(self):
        """ Función que define el flujo del API """
        type_services = TypeService.query.filter_by(
            deleted=False
        ).all()

        return type_services
