''' general.py: general functions '''
import math
from datetime import datetime
import pytz
from flask_babel import gettext
from libraries.utils import remove_extra_spaces
from libraries.response import entity_response  # pylint: disable=import-error

# pylint: disable=useless-else-on-loop, missing-function-docstring, super-init-not-called, dangerous-default-value, redefined-outer-name
def wrong_answer(msg, field):
    ''' Retorna respuesta erronea '''
    return entity_response(
        400,
        message="Invalid request",
        errors=[{
            'field': field,
            'message': gettext(msg),
            'extra': False
        }]
    )


def filter_(filters, type_, fields, value, mod=None):
    ''' Filtro en búsqueda '''
    if type_ == 1:
        filters.append({
            'type': 'or_multiple_like',
            'fields': fields,
            'value': ''.join(["*", remove_extra_spaces(value), "*"])
        })
    elif type_ == 2:
        filters.append({
            'type': 'match',
            'field': fields,
            'value': value
        })
    elif type_ == 3:
        filters.append({
            'type': 'date_range',
            'field': fields,
            'value': value,
            'date_math': mod
        })

def filter_alchemis(filters, type_, fields, value, mod=None):
    ''' Filtro en búsqueda '''
    if type_ == 1:
        filters.append({
            'type': 'or_multiple_like',
            'fields': fields,
            'value': remove_extra_spaces(value)
        })
    elif type_ == 2:
        filters.append({
            'type': 'match',
            'field': fields,
            'value': value
        })
    elif type_ == 3:
        filters.append({
            'type': 'date_range',
            'field': fields,
            'value': value,
            'date_math': mod
        })


def check_repeated_in_array(values):
    '''Retorna true si se repiten los elementos'''
    copy_values = values
    return len(set(copy_values)) != len(values)


def check_required_fields(data, fields):
    '''Retorna true si no hay campos requeridos'''
    for key in data.keys():
        if key in fields:
            return False
    else:
        return True


def check_membership_field(value, pool):
    """Retorna true si value pertenece a pool
    :param value: Puede ser un id de tipo entero
    :param pool: Puede ser un string con ids (separados por una coma) o una lista
    """
    if isinstance(pool, str):
        pool = pool.split(',')
        return str(value) in pool
    return value in pool


def check_value_equal(expr_1, expr_2, value):
    """checkea cuando se compara 2 campos con un valor"""
    return expr_1 == value and expr_2 != value


comparators = {
    'LESS_EQUAL': 'lte',
    'GREATER_EQUAL': 'gte',
    'LESS': 'lt',
    'GREATER': 'gt'
}


def check_page_limit(page, limit):
    '''Return true if paga and limir are 0'''
    return page == 0 and limit == 0


class FilterManager:
    """Clase para manejar filter de elasticsearch"""

    def __init__(self):
        self.filters = []

    def filter_by_search(self, fields, value):
        """Generar filtro por or_multiple_like"""
        self.filters.append({
            'type': 'or_multiple_like',
            'fields': fields,
            'value': ''.join(["*", remove_extra_spaces(value), "*"])
        })

    def filter_by_field(self, field, value):
        """Genera filtro por match"""
        self.filters.append({
            'type': 'match',
            'field': field,
            'value': value
        })

    def compare_by_date(self, field, value, comparator):
        """Genera filtro por date"""
        date = datetime.strptime(
            value, "%Y-%m-%dT%H:%M:%S.%f%z"
        )
        date = date.astimezone(pytz.timezone('UTC'))
        self.filters.append({
            'type': 'date_range',
            'field': field,
            'value': date.strftime("%Y-%m-%d %H:%M:%S"),
            'date_math': comparators[comparator]
        })

    def filter_not_match(self, field, value):
        """Genera filtro de no igual"""
        self.filters.append({
            'type': 'not_match',
            'field': field,
            'value': value
        })

    def filter_not_match_in_array(self, field, values):
        """Genera filtro de tipo not match"""
        for value in values:
            self.filter_not_match(field, value)

    def mapping_sort(self, model, sort):
        """Genera el mapping de sort"""
        if model.__mapping__[sort]["type"] == "text":
            sort = "{}.keyword".format(sort)
        return sort


def mapping_(model, filters, page, limit, sort, order):
    """Mapping"""
    if model.__mapping__[sort]["type"] == "text":
        sort = "%s.keyword" % sort
    result, total = model.search(filters, page, limit, sort, order)
    return result, total


def entity_response_search(result_, total, limit, page):
    """ Entity response to search"""
    return entity_response(
        200,
        message="The search has been successful",
        result=result_,
        pagination={
            'total': total,
            'page': page,
            'pages': math.ceil(total / limit)
        }
    )

class Filtro():
    '''Clase Lógica para hacer filtros'''
    def __init__(self):
        self.type = []
        self.field = None
        self.value = None
        self.conditional = True

    def get_response(self):

        if self.conditional is False or self.value is None:
            return None
        return self.handler_response()

    def handler_response(self):
        return None

class FiltroValue(Filtro):
    '''Clase Lógica filtrar valor'''
    def __init__(self, field, value, conditional=True):
        self.field = field
        self.value = value
        self.conditional = conditional

    def handler_response(self):
        return {
            'type': 'match',
            'field': self.field,
            'value': self.value
        }

class FiltroSearch(Filtro):
    '''Clase Lógica filtrar por busqueda'''
    def __init__(self, field, value, conditional=True):
        self.field = field
        self.value = value
        self.conditional = conditional

    def handler_response(self):
        return {
            'type': 'or_multiple_like',
            'fields': self.field,
            'value': ''.join(["*", remove_extra_spaces(self.value), "*"])
        }

class HandlerFilter():
    '''Clase lógica handler filter'''
    def __init__(self, arreglo=[]):
        self.filters = arreglo

    def get_response(self):
        response = []
        for filter_ in self.filters:
            answer = filter_.get_response()
            if answer is not None:
                response.append(answer)
        return response

class APIBusqueda():
    '''Clase lógica Api búsqueda'''
    def __init__(self, name_model, data, filters=[]):
        self.name_model = name_model
        self.filters = filters
        self.data = data

    def search(self):
        self.update_sort()
        page = self.data.get('page', False)
        limit = self.data.get('limit', False)
        sort = self.data.get('sort', False)
        order = self.data.get('order', False)
        return self.name_model.search(self.filters, page, limit, sort, order)

    def update_sort(self):
        if self.name_model.__mapping__[self.data['sort']]["type"] == "text":
            self.data['sort'] = "%s.keyword" % self.data['sort']

def accent(string):
    '''Elimina la tilde'''
    vowels_a, vowels_b = 'áéíóúñÁÉÍÓÚÑ', 'aeiounAEIOUN'
    trans = str.maketrans(vowels_a, vowels_b)
    return string.translate(trans)
