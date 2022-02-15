'''Manejador de excepción según lo que pidió Frontend'''


class HandlerByFrontend:
    '''Manejador de excepciones solicitado por Frontend'''

    def handle_exception(self, exception):
        '''Maneja una excepción según lo que pidio Frontend'''
        return exception.get_data()
