import datetime
from managers.class_utils.response.response_field import ResponseField
from libraries.utils import get_local_isoformat
class ModelField(ResponseField):
	'''Parent class for model field'''
	def __init__(self, field_name):
		self.field_name = field_name
		self.registry = None

	def get_field(self):
		field = {}
		if hasattr(self.registry, self.field_name):
			value_field = getattr(self.registry, self.field_name)
			if isinstance(value_field, datetime.datetime):
				value_field = get_local_isoformat(value_field)
			field[self.field_name] = value_field
		return field
