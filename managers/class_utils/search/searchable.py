'''searchable.py: Method file for search by query'''

from sqlalchemy import or_, and_
from functions.utils.util import remove_extra_spaces
from functions.general.general import accent
from managers.utils.manager_general import unaccent

def sort_by(cls, query, by_sort, by_order):
    '''Method to order a query'''
    if by_order:
        query = query.order_by(getattr(cls, by_sort).asc()) \
            if by_order == 'asc' else query.order_by(getattr(cls, by_sort).desc())
    return query.order_by(getattr(cls, by_sort))

def paginate(query, page, limit):
    '''Method to paginate a query'''
    return query.paginate(page=page, per_page=limit, error_out=False).query.all()

def set_filters(cls, filters):
    '''Method to filter queries'''
    queries = []
    for _filter in filters:
        if _filter['type'] == 'match':
            queries.append(getattr(cls, _filter['field']) == _filter['value'])
        if _filter['type'] == 'not_match':
            queries.append(getattr(cls, _filter['field']) != _filter['value'])
        if _filter['type'] == 'or_multiple_like':
            values = []
            for field in _filter['fields']:
                render_value = _filter['value']
                if isinstance(render_value, str):
                    render_value = accent(remove_extra_spaces(render_value))
                    values.append(unaccent(getattr(cls, field)).ilike('%{}%'.format(render_value)))
                else:
                    values.append(getattr(cls, field).ilike('%{}%'.format(render_value)))
            queries.append(or_(*values))
    final_query = cls.query.filter(
        and_(
            *queries
        )
    )
    return final_query

def render_filters(data):
    for key, value in six.iteritems(data):
        if isinstance(value, dict):
            render_filters(value)
        elif isinstance(value, str):
            data[key] = accent(remove_extra_spaces(value))
