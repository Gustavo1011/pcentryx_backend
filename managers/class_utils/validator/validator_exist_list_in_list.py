from exceptions.new_exceptions.not_exist_list_int_list_exception import NotExistListInListException
from managers.class_utils.validator.validator import Validator


class ValidatorExistListInList(Validator):
    """Class for validator Exist in list of values"""

    def __init__(self, lists_compare):
        self.field = 'unknown'
        self.lists = lists_compare
        self.code_error = 'ERROR-XXXXXXX'
        self.type_exception = 'DevelopmentException'
        self.description = 'List values not in compared list'

    def validate(self, data, vars_):
        flag, index = self.not_exist_in_list()
        if flag:
            raise NotExistListInListException(
                self.field, index, self.code_error,
                self.type_exception,  self.description,
            )

    def not_exist_in_list(self):
        field_list = self.lists.pop(0)
        for compare_list in self.lists:
            for index, value in enumerate(field_list):
                if value not in compare_list:
                    return True, index
        else:
            return False, None

    def set_code_error(self, code_error):
        self.code_error = code_error
        return self

    def set_field(self, field):
        self.field = field
        return self

    def set_type_exception(self, type_exception):
        self.type_exception = type_exception
        return self

    def set_description(self, description):
        self.description = description
        return self
