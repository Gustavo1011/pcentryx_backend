from managers.class_utils.response.response_field import ResponseField
from managers.class_utils.response.handler_response import HandlerResponse
from functions.utils.util import get_plural


class RelationHasMany(ResponseField):
	"""Parent class for relation has many"""
	def __init__(self, field_name, parts, deleted=False):
		super().__init__(get_plural(field_name))
		self.registry = None
		self.deleted = deleted
		self.parts = parts

	def get_field(self):
		field = {}
		if hasattr(self.registry, self.field_name):
			query = getattr(self.registry, self.field_name)
			response_object = query.filter_by(deleted=self.deleted).all()
			response_dicts = []
			for response_dict in response_object:
				handler = HandlerResponse(response_dict)
				handler.parts = self.parts
				response_dicts.append(handler.get_response())
			field[self.field_name] = response_dicts
		return field
