""" body_key_value.py: """
from libraries.line_code.line_code import LineCode


class BodyKeyValue(LineCode):
    """ Clase BodyKeyValue """

    def __init__(self, key, value, lines=None, identation=0):
        super().__init__()
        self.key = key
        self.value = value
        if lines is None:
            self.lines = []
        else:
            self.lines = lines
        self.identation = identation
        self.first_parameter = key

    def get_text(self):
        spaces = '  ' * self.identation
        text = spaces + '{}: {}'.format(self.key, self.value) + '\n'
        for line in self.lines:
            line.identation = self.identation + 1
            text += line.get_text()
        return text
