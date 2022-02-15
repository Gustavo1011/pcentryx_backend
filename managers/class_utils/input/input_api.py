class InputAPI():
	'''Parent class for input API'''
	def __init__(self):
		self.module_name = 'brands'
		self.tag = 'Brand Management'
		self.path_inputs = []
		self.query_inputs = []
		self.body_inputs = []
		self.type_request = 'GET'
		self.version = 'v4'
		self.description = 'Description'
		self.type_response = '200'
		self.snake_case = 'get_brand'

	def set_inputs(self):
		pass

	def set_path(self, inputs):
		self.path_inputs = inputs

	def set_query(self, inputs):
		self.query_inputs = inputs

	def set_body(self, inputs):
		self.body_inputs = inputs

	def get_structure(self):
		structure = {}
		for input_ in self.path_inputs:
			structure.update(input_.get_structure())
		for input_ in self.query_inputs:
			structure.update(input_.get_structure())
		for input_ in self.body_inputs:
			structure.update(input_.get_structure())
		return structure
