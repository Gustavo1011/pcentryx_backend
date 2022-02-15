from managers.class_utils.input.input_field import InputField


class InputBoolean(InputField):
	"""Parent class for input boolean"""
	def __init__(self, field_name, config={}, default=None):
		self.field_name = field_name
		self.config = config
		self.type = 'boolean'
		self.required = True
		self.default = default

	def get_structure(self):
		structure = {
			self.field_name: {
				'type': 'boolean',
				'required': True,
				'nullable': False,
				**self.config
			}
		}
		self.required = structure[self.field_name]['required']
		return structure
