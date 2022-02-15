'''Excepción nueva'''

class NewException(Exception):
    '''Clase para excepción nueva'''
    def __init__(self):
        super().__init__()
        self.value = None
