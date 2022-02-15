from managers.class_utils.input.input_field import InputField


class InputListIntegers(InputField):
    """Parent class for input list integers"""

    def __init__(self, field_name, input_config={}, config={}):
        super().__init__(field_name, config)
        self.input_config = input_config
        self.type = 'list_integers'
        self.required = True
        self.default = None

    def get_structure(self):
        structure = {
            self.field_name: {
                'type': 'list',
                'required': True,
                'minlength': 0,
                'schema': {
                    'type': 'integer',
                    'min': 0,
                    'max': 2147483648,
                    **self.input_config
                },
                **self.config
            }
        }
        self.required = structure[self.field_name]['required']
        return structure
