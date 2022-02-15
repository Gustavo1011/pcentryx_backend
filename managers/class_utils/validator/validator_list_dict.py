from managers.class_utils.validator.validator import Validator
from exceptions.not_exist_exception import NotExistException
from managers.utils.manager_general import ManagerGeneral


class ValidatorListDict(Validator):
    """Class for validator Exist"""
    def __init__(self, field_name, model_name, attr_name):
        self.field_name = field_name
        self.model_name = model_name
        self.attr_name = attr_name
        self.parts = []

    def validate(self, data):
        value = data.get(self.field_name)
        structure = {self.attr_name: value}
        if self.exist(structure) is False:
            raise self.get_exception(self.field_name)

    def exist(self, filters):
        """Verifica si existe ID"""
        manager = ManagerGeneral(self.model_name)
        manager.allow_deleted = False
        return manager.check_exist(filters)

    def get_exception(self, field):
        """Retorna una excepción de existencia"""
        return NotExistException(field)
