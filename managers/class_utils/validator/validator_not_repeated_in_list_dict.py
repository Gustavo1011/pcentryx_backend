from exceptions.new_exceptions.not_repeat_in_list_dict_exception import NotRepeatInListDictException
from managers.class_utils.validator.validator import Validator


class ValidatorNotRepeatedInListDict(Validator):
    """Class for validator for not repeat fields in list dict"""
    def __init__(self, field, sub_field):
        self.field = field
        self.sub_field = sub_field
        self.index = None

    def validate(self, data, vars_):
        value_list = data.get(self.field)
        if value_list is not None:
            if self.is_repeat(value_list):
                raise NotRepeatInListDictException(self.field, self.index)

    def is_repeat(self, value_list):
        values = []
        for value_dict in value_list:
            if value_dict[self.sub_field] in values:
                self.index = len(values)
                return True
            values.append(value_dict[self.sub_field])
        return False
