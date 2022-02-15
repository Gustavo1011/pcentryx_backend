class InputField():
	'''Parent class for input field'''
	def __init__(self, field_name, config={}):
		self.field_name = field_name
		self.config = config

	def get_structure(self):
		return {}
