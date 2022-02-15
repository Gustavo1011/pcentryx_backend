""" tag_value.py: """
from libraries.line_code.line_code import LineCode


class TagValue(LineCode):
    """ Clase TagValue """

    def __init__(self, name, lines=None, identation=0):
        super().__init__()
        self.name = name
        if lines is None:
            self.lines = []
        else:
            self.lines = lines
        self.identation = identation
        self.first_parameter = name

    def get_text(self):
        spaces = '  ' * self.identation
        text = spaces + '- {}'.format(self.name) + '\n'
        for line in self.lines:
            line.identation = self.identation + 1
            text += line.get_text()
        return text
