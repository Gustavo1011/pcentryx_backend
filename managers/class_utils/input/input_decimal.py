from managers.class_utils.input.input_field import InputField

class InputDecimal(InputField):
	"""Parent class for input integer"""
	def __init__(self, field_name, config={}, default=None):
		super().__init__(field_name, config)
		self.type = 'number'
		self.required = True
		self.default = default

	def get_structure(self):
		structure = {
			self.field_name: {
				'type': 'number',
				'required': True,
				'nullable': False,
				'min': 0,
				**self.config
			}
		}
		self.required = structure[self.field_name]['required']
		return structure
