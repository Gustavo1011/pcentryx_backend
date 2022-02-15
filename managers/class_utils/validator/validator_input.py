from libraries.validator import Validator
from exceptions.new_exceptions.structure_exception import StructureException

class ValidatorInput(Validator):
    '''Class for validator Input'''
    def __init__(self, module):
        self.module = module

    def validate(self, data, vars):
        structure = self.module.input_api.get_structure()
        validator = Validator(structure)
        validator.validate(data)
        if validator.errors:
            raise StructureException(validator.errors)
