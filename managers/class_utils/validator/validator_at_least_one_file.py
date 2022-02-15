from exceptions.new_exceptions.not_at_least_one_file_exception import NotAtLeastOneFileException
from functions.utils.util import get_model
from managers.class_utils.validator.validator import Validator


class ValidatorAtLeastOneFile(Validator):
    """Class for validator at Least One File"""

    def __init__(self, model, field_model, field_data):
        self.model = get_model(model)
        self.field_model = field_model
        self.field_data = field_data
        self.field_to_delete = 'Unknow'
        self.code_error = 'ERROR-XXXXXXX'
        self.type_exception = 'CustomerException'
        self.description = 'At least one file is required'
        self.query = None

    def validate(self, data, vars_):
        current_files = self.get_files(data)
        if len(current_files) < len(data[self.field_to_delete]):
            raise NotAtLeastOneFileException(
                self.field_to_delete, self.code_error,
                self.type_exception, self.description
            )

    def get_files(self, data):
        self.query = self.model.query.filter(
            getattr(self.model, self.field_model) == data[self.field_data],
        ).first()
        files = self.query.get_files()
        drive_ids = []
        for file in files:
            drive_ids.append(file.drive_id)
        return drive_ids

    def set_field_to_delete(self, files_to_delete):
        self.field_to_delete = files_to_delete
        return self

    def set_code_error(self, code_error):
        self.code_error = code_error
        return self

    def set_type_exception(self, type_exception):
        self.type_exception = type_exception
        return self

    def set_description(self, description):
        self.description = description
        return self
