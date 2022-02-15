from managers.class_utils.input.input_field import InputField


class InputInteger(InputField):
	"""Parent class for input integer"""
	def __init__(self, field_name, config={}, default=None):
		super().__init__(field_name, config)
		self.type = 'integer'
		self.required = True
		self.default = default

	def get_structure(self):
		structure = {
			self.field_name: {
				'type': 'integer',
				'required': True,
				'nullable': False,
				'min': 1,
				'max': 2147483648,
				**self.config
			}
		}
		self.required = structure[self.field_name]['required']
		return structure
