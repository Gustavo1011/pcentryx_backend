from managers.class_utils.validator.validator import Validator
from managers.class_utils.validator.field_v2 import FieldV2

class IterateListDictV3(Validator):
    """class to add a for in validators"""
    def __init__(self, list_name, validators=[]):
        self.list_name = list_name
        self.validators = validators
        self.parent_data = {}
        self.parent_key_error = ''
        self.list_data = []
        self.data = {}

    def validate(self, data, vars_):
        field = FieldV2(self.list_name)
        field.list_data = self.list_data
        list_elements = field.get_value(data, self.parent_data)
        for index, element in enumerate(list_elements):
            for validator in self.validators:
                validator.parent_data = element
                validator.list_data = [{**element}, *self.list_data]
                validator.parent_key_error = '{}{}.{}.'.format(
                    self.parent_key_error, self.list_name, index
                )
                validator.validate(data, vars_)
