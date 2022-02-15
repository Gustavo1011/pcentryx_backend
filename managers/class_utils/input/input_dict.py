from managers.class_utils.input.input_field import InputField

class InputDict(InputField):
	"""Parent class for input dict"""
	def __init__(self, field_name, inputs=[], config={}):
		super().__init__(field_name, config)
		self.inputs = inputs
		self.type = 'dict'
		self.required = True

	def get_structure(self):
		internal_structure = {}
		for input_ in self.inputs:
			internal_structure.update(input_.get_structure())
		structure = {
			self.field_name: {
				'type': 'dict',
				'required': True,
				'nullable': False,
				'schema': internal_structure,
				**self.config
			}
		}
		self.required = structure[self.field_name]['required']
		return structure
