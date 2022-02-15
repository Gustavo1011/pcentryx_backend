from managers.class_utils.response.response_field import ResponseField
from managers.class_utils.response.handler_response import HandlerResponse
class FunctionDict(ResponseField):
	'''Parent class for model field'''
	def __init__(self, field_name, alias, parts=[]):
		self.field_name = field_name
		self.registry = None
		self.parts = parts
		self.alias = alias

	def get_field(self):
		field = {}
		if hasattr(self.registry, self.field_name):
			response_object = getattr(self.registry, self.field_name)()
			if isinstance(response_object, list):
				response_dicts = []
				for response_dict in response_object:
					handler = HandlerResponse(response_dict)
					handler.parts = self.parts
					response_dicts.append(handler.get_response())
				field[self.alias] = response_dicts
			else:
				response_dict = {}
				handler = HandlerResponse(response_object)
				handler.parts = self.parts
				response_dict.update(handler.get_response())
				field[self.alias] = response_dict
		return field
