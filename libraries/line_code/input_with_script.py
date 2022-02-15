""" input_with_script.py: """
from libraries.line_code.line_code import LineCode


class InputWithScript(LineCode):
    """ Class InputWithScript """

    def __init__(self, type_, lines=None, identation=0):
        super().__init__()
        self.type = type_
        if lines is None:
            self.lines = []
        else:
            self.lines = lines
        self.identation = identation
        self.first_parameter = type_

    def get_text(self):
        spaces = '  ' * self.identation
        text = spaces + '- in: {}'.format(self.type) + '\n'
        for line in self.lines:
            line.identation = self.identation + 1
            text += line.get_text()
        return text
