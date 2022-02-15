""" input_field_value.py: Genera swagger por linea """
from libraries.line_code.line_code import LineCode


class InputFieldValue(LineCode):
    """ Clase para generar swagger por linea """
    def __init__(self, field, value, lines=None, identation=0):
        super().__init__()
        self.field = field
        self.value = value
        if lines is None:
            self.lines = []
        else:
            self.lines = lines
        self.identation = identation
        self.first_parameter = field

    def get_text(self):
        spaces = '  ' * self.identation
        text = spaces + '{}: {}'.format(self.field, self.value) + '\n'
        for line in self.lines:
            line.identation = self.identation + 1
            text += line.get_text()
        return text
