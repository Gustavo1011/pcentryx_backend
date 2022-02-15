from managers.class_utils.response.handler_response import HandlerResponse
class ResponseAPI():
	'''Parent class for response API'''
	def __init__(self):
		self.model_name = 'Brand'
		self.value = None
		self.handler = None

	def set_response(self):
		pass

	def set_value(self, value):
		self.value = value

	def set_structure(self, parts):
		self.handler = HandlerResponse(self.value)
		self.handler.parts = parts

	def get_response(self):
		self.set_response()
		return self.handler.get_response()


