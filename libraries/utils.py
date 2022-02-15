"""
utils.py: Librería para utilidades
"""

import re
from datetime import datetime
import pytz
from sqlalchemy import and_
from sqlalchemy.orm import aliased
import stringcase
from flask_jwt_extended import get_jwt_identity

def snake_case(value):
    ''' Convierte un string en Snake Case '''
    case = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', case).lower()

def get_model(model, snake=True):
    ''' Obtiene la clase según modelo '''
    file = snake_case(model) if snake else model
    class_name = model if snake else stringcase.pascalcase(model)
    entity_module = __import__('models.%s' % file, fromlist=[class_name])
    return getattr(entity_module, class_name)

def get_dependencies(entity, value, current_aliased=False):
    ''' Obtiene la lista de dependecias en recursiva según modelo '''
    entity_value = entity.first()
    model = get_model(value) if not current_aliased \
        else aliased(get_model(value), name=current_aliased + "_" + value)
    if hasattr(model, '__dependencies__'):
        dependencies = getattr(model, '__dependencies__')
        for dependency in dependencies:
            if dependency[2] == "CASCADE":
                field_model = dependency[1]
                if hasattr(entity_value, field_model) and getattr(entity_value, field_model):
                    current_model_name = dependency[3] if len(dependency) > 3 else value
                    current_model = aliased(
                        get_model(dependency[3]),
                        name=value + "_" + dependency[3]
                    ) if len(dependency) > 3 else model
                    model_dependency = aliased(get_model(dependency[0]), \
                        name=current_model_name + "_" + dependency[0])
                    entity = entity.join(model_dependency, and_(
                        model_dependency.id == getattr(current_model, field_model),
                        model_dependency.deleted == "false"
                    ))
                    entity = get_dependencies(entity, dependency[0], value)
    return entity

def dec2string_stripped(num, dec_places=3, strip='right'):
    """
    Parameters
    ----------
    num : float or list of float
        scalar or list of decimal numbers.
    dec_places : int, optional
        number of decimal places to return. defaults to 3.
    strip : string, optional
        what to strip. 'right' (default), 'left' or 'both'.

    Returns
    -------
    list of string.
        numbers formatted as strings according to specification (see kwargs).
    """
    if not isinstance(num, list): # might be scalar or numpy array
        try:
            num = list(num)
        except TypeError: # input was scalar
            num = [num]

    if not isinstance(dec_places, int) or int(dec_places) < 1:
        raise ValueError(f"kwarg dec_places must be integer > 1 (got {dec_places})")

    formats = []
    if strip == 'right':
        formats = [f"{n:.{str(dec_places)}f}".rstrip('0') for n in num]
    if strip == 'left':
        formats = [f"{n:.{str(dec_places)}f}".lstrip('0') for n in num]
    if strip == 'both':
        formats = [f"{n:.{str(dec_places)}f}".strip('0') for n in num]
    if formats:
        result = []
        for item in formats:
            if item.endswith('.'):
                item = item[:-1]
            result.append(item)
        if len(result) == 1:
            return result[0]
        return result
    raise ValueError(f"kwarg 'strip' must be 'right', 'left' or 'both' (got '{strip}')")


def is_equal_lists(list_a, list_b):
    """ Determina si dos listas son iguales """
    if len(list_a) != len(list_b):
        return False

    list_a.sort()
    list_b.sort()

    for index, item in enumerate(list_a):
        if item != list_b[index]:
            return False

    return True


def is_duplicated_in_list(list_a):
    """ Determina si hay elementos repetidos en una lista """
    list_b = list(set(list_a))
    list_a.sort()
    list_b.sort()

    return list_a != list_b


def remove_extra_spaces(sentence):
    """ Quita los espacios en blanco extras """
    result = re.sub(r'^\s+|\s+$', '', sentence, flags=re.UNICODE)
    return re.sub(r'\s+', ' ', result, flags=re.UNICODE)

def get_local_isoformat(date_utc):
    """
        Obtiene formato fecha local de un datetime sin timezone
        El timezone proviene de la sesión
    """
    if date_utc is None:
        return None
    current_user = get_jwt_identity()
    if current_user is None:
        pytz_timezone = pytz.timezone('UTC')
    else:
        if current_user['timezone'] is not None:
            pytz_timezone = pytz.timezone(current_user['timezone'])
        else:
            end_token = datetime.strptime(
                current_user['end_token'], "%Y-%m-%dT%H:%M:%S.%f%z"
            )
            pytz_timezone = end_token.tzinfo
    date_local = date_utc.astimezone(pytz_timezone)
    return date_local.isoformat(timespec='milliseconds')

def get_now(timezone='UTC'):
    """ Obtiene la hora del sistema según la zona horaria indicada """
    return datetime.now(pytz.timezone(timezone))
