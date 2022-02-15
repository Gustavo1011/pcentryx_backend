from managers.class_utils.validator.validator import Validator

class IterateListDictV2(Validator):
    """class to add a for in validators"""
    def __init__(self, list_name, validators=[]):
        self.list_name = list_name
        self.validators = validators
        self.parent_data = {}
        self.parent_key_error = ''
        self.list_data = []

    def validate(self, data, vars_):
        for index, element in enumerate(data.get(self.list_name)):
            for validator in self.validators:
                validator.parent_data = element
                validator.list_data = [{**element}, *self.list_data]
                validator.parent_key_error = '{}{}.{}.'.format(
                    self.parent_key_error, self.list_name, index
                )
                validator.validate(data, vars_)
