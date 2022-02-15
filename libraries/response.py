''' Módulo para construir para una respuesta HTTP para API '''
import copy
from flask_babel import gettext # pylint: disable=import-error

def entity_response(code, message=False, errors=False, result=False, pagination=False):
    ''' Función para retornar una respuesta HTTP '''
    return {
        "errors": errors,
        "message": gettext(message),
        "result": result,
        "pagination": pagination
    }, code

def request_response(items):
    ''' Función para retornar una respuesta HTTP '''
    errors = []
    for name, messages in items:
        error = {
            'field': name
        }
        get_response(error, messages, errors)

    return {
        'errors': errors,
        'message': gettext("Invalid request"),
        'result': False,
        'pagination': False
    }, 400

def get_response(error, messages, errors):
    ''' Funcion recursiva usada para obtener la respuesta de error '''
    for msg in messages:
        if isinstance(msg, dict):
            for index, error_array in msg.items():
                _error = copy.deepcopy(error)
                aux = _error
                if isinstance(index, int):
                    while 'extra' in aux:
                        aux = aux['extra']
                    aux['extra'] = {
                        'index': index
                    }
                else:
                    while 'extra' in aux:
                        aux = aux['extra']
                    if 'index' in aux:
                        aux['field'] = index
                    else:
                        aux['extra'] = {
                            'field': index
                        }
                get_response(_error, error_array, errors)
        else:
            _error = copy.deepcopy(error)
            _error['message'] = msg
            aux = _error
            while 'extra' in aux:
                aux = aux['extra']
            if 'field' not in aux:
                aux['field'] = 'value'
            errors.append(_error)

def dependencies_error(field, message, result):
    ''' Retornar mensaje de error para los casos de bloqueo por dependencias '''
    return {
        'errors': [{
            'field': field,
            'message': gettext(message),
            'extra': False
        }],
        'message': gettext("Invalid request"),
        'result': result,
        'pagination': False
    }, 400
