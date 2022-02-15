from managers.class_utils.input.input_field import InputField


class InputString(InputField):
	"""Parent class for input string"""
	def __init__(self, field_name, config={}, default=None):
		super().__init__(field_name, config)
		self.type = 'string'
		self.required = True
		self.default = default

	def get_structure(self):
		structure = {
			self.field_name: {
				'type': 'string',
				'required': True,
				'nullable': False,
				'minlength': 1,
				'maxlength': 250,
				**self.config
			}
		}
		self.required = structure[self.field_name]['required']
		return structure
