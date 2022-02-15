from managers.class_utils.response.response_field import ResponseField

class MethodValue(ResponseField):
	'''Parent class for method value field'''
	def __init__(self, method_name, key_name):
		self.method_name = method_name
		self.key_name = key_name
		self.registry = None

	def get_field(self):
		field = {}
		if hasattr(self.registry, self.method_name):
			value_field = getattr(self.registry, self.method_name)
			field[self.key_name] = value_field()
		return field
