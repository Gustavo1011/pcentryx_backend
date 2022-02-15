from managers.class_utils.input.input_field import InputField


class InputListStrings(InputField):
	"""Parent class for input list strings"""
	def __init__(self, field_name, input_config={}, config={}):
		super().__init__(field_name, config)
		self.input_config = input_config
		self.type = 'list_strings'
		self.required = True

	def get_structure(self):
		structure = {self.field_name: {
			'type': 'list',
			'required': True,
			'minlength': 0,
			'schema': {
				'type': 'string',
				'minlength': 1,
				'maxlength': 250,
				**self.input_config
			},
			**self.config
		}}
		self.required = structure[self.field_name]['required']
		return structure
