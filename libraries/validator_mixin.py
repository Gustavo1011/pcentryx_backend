''' Librería para validar entidad de modelo de datos '''

from flask_babel import gettext
from libraries.utils import get_model, get_dependencies

class ValidatorMixin(): # pylint: disable=too-few-public-methods
    ''' Clase para validar entidad de modelo de datos '''

    @classmethod
    # pylint: disable=too-many-branches, too-many-locals
    def validate(cls, request, entity_id=False):
        ''' Valida reglas de entidad de modelo de datos '''
        # pylint: disable=line-too-long
        for key in cls.__rules__:
            if key in request and request[key] is not None:
                rules = cls.__rules__[key]
                for row in rules:
                    if (row['rule'] == 'exist' or row['rule'] == 'not_exist') \
                    and key in request and request[key] is not None:
                        entity_class = get_model(row['model'])
                        if 'insensitive' in row and row['insensitive']:
                            main_filter = getattr(entity_class, row['field']).ilike(request[key])
                        else:
                            main_filter = getattr(entity_class, row['field']) == request[key]
                        entity = entity_class.query.filter(main_filter)
                        if not 'deleted' in row:
                            entity = entity.filter(entity_class.deleted == "false")
                        if 'without_itself' in row and row['without_itself'] and entity_id:
                            entity = entity.filter(getattr(entity_class, 'id') != entity_id)

                        entity = get_dependencies(entity, row['model'])

                        entity = entity.first()
                        if (row['rule'] == 'exist' and entity is None) or \
                        (row['rule'] == 'not_exist' and entity is not None):
                            return {
                                'valid': False,
                                'result': {
                                    'errors': [{
                                        'field': key,
                                        'message': gettext(row['message']),
                                        'extra': False
                                    }],
                                    'message': gettext("Invalid request"),
                                    'result': False,
                                    'pagination': False
                                }
                            }

                    if row['rule'] == 'no_repeat_in_array':
                        used = []
                        for index, entity_value in enumerate(request[key]):
                            if isinstance(entity_value, dict) and not row['of_field'] in entity_value:
                                continue
                            value = entity_value[row['of_field']] if isinstance(entity_value, dict) \
                                else entity_value
                            if value in used:
                                return {
                                    'valid': False,
                                    'result': {
                                        'errors': [{
                                            'field': key,
                                            'message': gettext(row['message']),
                                            'extra': {
                                                "of_fields": row['of_field'],
                                                "index": index
                                            }
                                        }],
                                        'message': gettext("Invalid request"),
                                        'result': False,
                                        'pagination': False
                                    }
                                }
                            used.append(value)

                    if row['rule'] == 'no_itself_in_array':
                        used = []
                        for index, entity_value in enumerate(request[key]):
                            value = entity_value[row['of_field']] if isinstance(entity_value, dict) else \
                                entity_value
                            if value == entity_id:
                                return {
                                    'valid': False,
                                    'result': {
                                        'errors': [{
                                            'field': key,
                                            'message': gettext(row['message']),
                                            'extra': {
                                                "of_fields": row['of_field'],
                                                "index": index
                                            }
                                        }],
                                        'message': gettext("Invalid request"),
                                        'result': False,
                                        'pagination': False
                                    }
                                }

                    if row['rule'] == 'exist_in_array' or row['rule'] == 'not_exist_in_array':
                        entity_class = get_model(row['model'])

                        for index, entity_value in enumerate(request[key]):

                            if isinstance(entity_value, dict) and not row['of_field'] in entity_value:
                                continue
                            value = entity_value[row['of_field']] if isinstance(entity_value, dict) else \
                                entity_value
                            entity = entity_class.query.filter(
                                getattr(entity_class, row['field']) == value
                            )
                            if not 'deleted' in row:
                                entity = entity.filter(entity_class.deleted == "false")

                            if 'without_itself' in row and row['without_itself'] and 'id' in entity_value:
                                entity = entity.filter(getattr(entity_class, 'id') != entity_value['id'])

                            entity = get_dependencies(entity, row['model'])

                            entity = entity.first()
                            if (row['rule'] == 'exist_in_array' and entity is None) or \
                            (row['rule'] == 'not_exist_in_array' and entity is not None):
                                return {
                                    'valid': False,
                                    'result': {
                                        'errors': [{
                                            'field': key,
                                            'message': gettext(row['message']),
                                            'extra': {
                                                "of_fields": row['of_field'],
                                                "index": index
                                            }
                                        }],
                                        'message': gettext("Invalid request"),
                                        'result': False,
                                        'pagination': False
                                    }
                                }

                    if row['rule'] == 'restrict_in_array':
                        entity_class = get_model(row['model'])

                        for index, entity_value in enumerate(request[key]):

                            if isinstance(entity_value, dict) and not row['of_field'] in entity_value:
                                continue
                            value = entity_value[row['of_field']] if isinstance(entity_value, dict) else \
                                entity_value

                            entity = entity_class.query.filter(
                                getattr(entity_class, row['of_field']) == value,
                                getattr(entity_class, row['compare_field']) == request[row['field']]
                            ).first()

                            if entity is None:
                                return {
                                    'valid': False,
                                    'result': {
                                        'errors': [{
                                            'field': key,
                                            'message': gettext(row['message']),
                                            'extra': {
                                                "of_fields": row['of_field'],
                                                "index": index
                                            }
                                        }],
                                        'message': gettext("Invalid request"),
                                        'result': False,
                                        'pagination': False
                                    }
                                }

        return {
            'valid': True
        }
