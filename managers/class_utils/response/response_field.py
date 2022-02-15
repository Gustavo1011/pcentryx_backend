class ResponseField():
	'''Parent class for response field'''
	def __init__(self, field_name):
		self.field_name = field_name
		self.registry = None

	def get_field(self):
		return {}
