import re
from managers.class_utils.validator.validator import Validator
from functions.utils.util import get_model, snake_case
from exceptions.new_exceptions.not_enabled_exist_in_list_dict_exception import NotEnabledExistInListDictException

class ValidatorEnabledExistInListDict(Validator):
    """Class to validate that an attribute of an dictionary is not repeated"""
    def __init__(self, model, field_model, name_dicts, attribute_name):
        self.model = get_model(model)
        self.field_model = field_model
        self.name_dicts = name_dicts
        self.attribute_name = attribute_name
        self.deleted = [getattr(self.model, 'deleted') == "False"]
        self.enabled = [getattr(self.model, 'is_enabled') == "True"]
        self.query = None
        self.index = 0

    def validate(self, data, vars_):
        if self.not_enabled_exist(data) is True:
            raise NotEnabledExistInListDictException(
                field=self.name_dicts, index=self.index,
                name_value=self.attribute_name
            )

    def not_enabled_exist(self, data):
        for index, element in enumerate(data.get(self.name_dicts)):
            self.query = self.model.query.filter(
                getattr(self.model, self.field_model) == element.get(self.attribute_name),
                *self.deleted,
                *self.enabled
            )
            if self.query.count() == 0:
                self.index = index
                return True
