from managers.class_utils.response.response_field import ResponseField
from managers.class_utils.response.handler_response import HandlerResponse


class RelationHasOne(ResponseField):
	"""Parent class for relation has one"""
	def __init__(self, field_name, parts, deleted=False):
		super().__init__(field_name)
		self.registry = None
		self.deleted = deleted
		self.parts = parts

	def get_field(self):
		field = {}
		if hasattr(self.registry, self.field_name):
			response_object = getattr(self.registry, self.field_name)
			response_dict = {}
			handler = HandlerResponse(response_object)
			handler.parts = self.parts
			response_dict.update(handler.get_response())
			field[self.field_name] = response_dict
		return field
