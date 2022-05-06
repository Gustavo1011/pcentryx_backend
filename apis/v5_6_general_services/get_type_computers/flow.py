""" Define el flujo para el API get_type_computers """
from models.type_computer import TypeComputer

class GetTypeComputersFlow:
    """ Clase para definir el flujo del API get_type_computers """
    def __init__(self):
        """ Constructor de la clase """
        self.data = None

    def action(self):
        """ Función que define el flujo del API """

        type_computers = TypeComputer.query.filter_by(
            deleted=False
        ).all()

        return type_computers
