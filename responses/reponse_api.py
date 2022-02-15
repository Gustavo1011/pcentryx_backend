'''reponse_api.py: File to manage a reponse'''
from flask_babel import gettext
from .status_messages import StatusMessages
from .pagination_response import PaginationResponse

class ResponseApi(StatusMessages, PaginationResponse):
    '''Clase para manejar las respuestas de API'''

    def __init__(self, code, result, key_responses=None):
        PaginationResponse.__init__(self)
        StatusMessages.__init__(self)
        self.key_responses = key_responses
        self.code = code
        self.result = result
        self.message = self.status_messages[self.code]
        self.errors = False

    def entity_response(self):
        '''Función para retornar una respuesta HTTP'''
        self.process_result()
        return {
            "errors": self.errors,
            "message": gettext(self.message),
            "result": self.result,
            "pagination": self.pagination
        }, self.code

    def process_result(self):
        '''Obtener respuesta de todos los objetos enviados'''
        keys = {} if self.key_responses is None else self.key_responses
        if isinstance(self.result, list):
            self.result = list(map(lambda x: x.get_response(**keys), self.result))
        else:
            self.result = self.result.get_response(**keys)
