from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.not_exist_exception import NotExistException
from functions.utils.util import (
    get_model, get_operator
)
from functions.general.general import accent
from managers.utils.manager_general import unaccent

class ValidatorExistInBDV2(Validator):
    """class to validate that there is a record in the database"""
    def __init__(self, model_name, filters=[], key_error='Unknown', key='unknown', has_filter_deleted=True):
        self.model = get_model(model_name)
        self.filters = filters
        self.key_error = key_error
        self.key = key
        self.parent_data = {}
        self.list_data = []
        self.parent_key_error = ''
        self.has_filter_deleted = has_filter_deleted

    def validate(self, data, vars_):
        if self.is_exist(self.parent_data) is False:
            filter_keys = []
            for filter_ in self.filters:
                filter_keys.append(filter_[0])
            raise NotExistException(
                self.parent_key_error + self.key_error,
                filter_keys
            )

    def is_exist(self, data):
        new_filters = []
        for filter_ in self.filters:
            operator = get_operator(filter_[1])
            if filter_[2].__class__.__name__ == 'FieldV2':
                filter_[2].list_data = self.list_data
                value = filter_[2].get_value(data, self.parent_data)
                value = self.parent_data.get(filter_[2].name)
            else:
                value = filter_[2]
            if isinstance(value, str) and filter_[1] == "==" and value not in ['True', 'true', 'False', 'false']:
                new_filters.append(
                    unaccent(getattr(self.model, filter_[0])).ilike('{}'.format(accent(value)))
                )
            elif isinstance(value, bool):
                new_filters.append(operator(getattr(self.model, filter_[0]), str(value)))
            else:
                new_filters.append(operator(getattr(self.model, filter_[0]), value))
        filter_deleted = []
        if self.has_filter_deleted is True:
            filter_deleted.append(getattr(self.model, 'deleted') == "False")
        registry = self.model.query.filter(
            *filter_deleted,
            *new_filters
        ).first()
        if registry is not None:
            self.parent_data[self.key] = registry
            if len(self.list_data) > 1:
                self.list_data[1][self.key] = registry
            return True
        return False
