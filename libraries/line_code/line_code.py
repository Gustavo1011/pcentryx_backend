""" Define linea de codigo para generar el swagger """


class LineCode:
    """ Clase linea de codigo para swagger """

    def __init__(self):
        self.lines = []
        self.first_parameter = None

    def get_text(self):
        """ get_text method """
        return ''

    def __eq__(self, other):
        return self.first_parameter == other.first_parameter
