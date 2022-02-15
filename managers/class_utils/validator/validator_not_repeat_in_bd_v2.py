from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.unique_exception import UniqueException
from functions.utils.util import (
    get_model, get_operator
)
from functions.general.general import accent
from managers.utils.manager_general import unaccent

class ValidatorNotRepeatInBDV2(Validator):
    """Class to validate that DB record fields are not repeated"""
    def __init__(self, model_name, filters=[], key_error='Unknown', has_filter_deleted=True):
        self.model = get_model(model_name)
        self.filters = filters
        self.key_error = key_error
        self.parent_data = {}
        self.parent_key_error = ''
        self.has_filter_deleted = has_filter_deleted

    def validate(self, data, vars_):
        if self.is_exist(self.parent_data) is True:
            filter_keys = []
            for filter_ in self.filters:
                filter_keys.append(filter_[0])
            raise UniqueException(
                self.parent_key_error + self.key_error,
                filter_keys
            )

    def is_exist(self, data):
        new_filters = []
        for filter_ in self.filters:
            operator = get_operator(filter_[1])
            if filter_[2].__class__.__name__ == 'FieldV2':
                value = self.parent_data.get(filter_[2].name)
            else:
                value = filter_[2]
            if isinstance(value, str) and filter_[1] == "==" and value not in ['True', 'true', 'False', 'false']:
                new_filters.append(
                    getattr(self.model, filter_[0]).ilike('{}'.format(accent(value)))
                )
            elif isinstance(value, bool):
                new_filters.append(operator(getattr(self.model, filter_[0]), str(value)))
            else:
                new_filters.append(operator(getattr(self.model, filter_[0]), value))
        filter_deleted = []
        if self.has_filter_deleted is True:
            filter_deleted.append(getattr(self.model, 'deleted') == "False")
        return self.model.query.filter(
            *filter_deleted,
            *new_filters
        ).count() > 0
