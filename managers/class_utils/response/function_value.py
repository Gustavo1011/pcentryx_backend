from managers.class_utils.response.response_field import ResponseField


class FunctionValue(ResponseField):
	"""Parent class for function value"""
	def __init__(self, field_name, alias):
		super().__init__(field_name)
		self.registry = None
		self.alias = alias

	def get_field(self):
		field = {}
		if hasattr(self.registry, self.field_name):
			response_object = getattr(self.registry, self.field_name)()
			field[self.alias] = response_object
		return field
