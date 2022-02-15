""" util.py: util functions """
import re
import operator
import stringcase
import six


def check_field_required_in_dictionary(
        dictionary, field_name,
        message='Required field'
):
    """ Check field required in dictionary """
    if field_name not in dictionary:
        raise Exception({
            'name': 'RequiredFieldError',
            'field': field_name,
            'message': message,
            'extra': False
        })


def check_field_not_required_in_dictionary(
        dictionary, field_name,
        message='Field not required'
):
    """ Check field not required in dictionary """
    if field_name in dictionary:
        raise Exception({
            'name': 'RequiredFieldError',
            'field': field_name,
            'message': message,
            'extra': False
        })


def snake_case(value):
    """ Convierte un string en Snake Case """
    case = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', case).lower()


def get_plural(value):
    """ Obtiene plural de un string """
    if value[-1] == 'y':
        return value[0:-1] + 'ies'
    if value[-1] == 's':
        return value[0:-1] + 'ses'
    if value[-1] == 'h' and value[-2] == 'c':
        return value[0:-1] + 'hes'
    return value + 's'


def get_model(model, snake=True):
    """ Obtiene la clase según modelo """
    file = snake_case(model) if snake else model
    class_name = model if snake else stringcase.pascalcase(model)
    entity_module = __import__('models.%s' % file, fromlist=[class_name])
    return getattr(entity_module, class_name)


def remove_spaces_in_dict(data):
    """Remueve los espacios extras de un diccionario"""
    for key, value in six.iteritems(data):
        if isinstance(value, dict):
            remove_spaces_in_dict(value)
        elif isinstance(value, str):
            data[key] = remove_extra_spaces(value)


def remove_extra_spaces(sentence):
    """ Quita los espacios en blanco extras """
    result = re.sub(r'^\s+|\s+$', '', sentence, flags=re.UNICODE)
    return re.sub(r'\s+', ' ', result, flags=re.UNICODE)


operators = {
    '==': 'eq',
    '<=': 'le',
    '>=': 'ge',
    '<': 'lt',
    '>': 'gt',
    '!=': 'ne'
}


def get_operator(symbol):
    """Obtiene operador"""
    return getattr(operator, operators[symbol])


def not_none(expr_1, expr_2):
    """Retorna booleano"""
    return expr_1 is not None and expr_2 is None


def get_fields_mapping(model_name):
    """ Obtiene los campos del mapping del modelo """
    model = get_model(model_name)
    constraints = list(model.__dict__['__table__'].__dict__['constraints'])
    constraint = None
    for key in constraints:
        if key.__class__.__name__ == 'CheckConstraint':
            constraint = key

    # pylint: disable=line-too-long
    fields_mapping = re.findall(r"Column\(\'([a-zA-Z_]*)\', ([a-zA-Z]*)\([a-zA-Z=0-9, ]*\),", str(constraint))
    return dict(fields_mapping)


def get_field_of_dict(field_data, data):
    """ Obtener campo de un diccionario"""
    locates = field_data.split('.')
    local_data = data
    for locate in locates:
        if isinstance(locate, str):
            local_data = local_data[locate]
    return local_data


def get_antisort(value):
    """ Funcion utilizada para busquedas con ordenamiento booleando """
    if value == "asc":
        return "desc"
    return "asc"

