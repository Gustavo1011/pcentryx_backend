from managers.class_utils.validator.validator import Validator
from exceptions.new_exceptions.not_repeat_in_list_dict_exception import NotRepeatInListDictException

class ValidatorNotRepeatInListDictV2(Validator):
    """Class to validate that an attribute of an dictionary is not repeated"""
    def __init__(self, name_dicts, attribute_name, key_error='Unknown', key='unknown'):
        self.name_dicts = name_dicts
        self.attribute_name = attribute_name
        self.index = 0
        self.key_error = '{}.{}'.format(name_dicts, attribute_name)
        self.key = key
        self.parent_data = {}
        self.parent_key_error = ''

    def validate(self, data, vars_):
        if self.has_repetition(self.parent_data) is True:
            raise NotRepeatInListDictException(
                field=self.parent_key_error+self.key_error,
                index=self.index
            )

    def has_repetition(self, data):
        list_values = []
        for index, element in enumerate(data.get(self.name_dicts)):
            if element.get(self.attribute_name) in list_values:
                self.index = index
                return True
            list_values.append(element.get(self.attribute_name))
        return False
