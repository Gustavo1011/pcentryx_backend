'''Manejador simple de excepciones'''


class SimpleHandler:
    '''Manejador simple de excepción'''

    def handle_exception(self, exception):
        '''Maneja una excepción de forma simple'''
        return exception.get_response()
