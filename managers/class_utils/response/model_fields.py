import datetime
from managers.class_utils.response.response_field import ResponseField
from libraries.utils import get_local_isoformat
from functions.utils.util import get_fields_mapping
class ModelFields(ResponseField):
	'''Parent class for model field'''
	def __init__(self):
		self.registry = None

	def get_field(self):
		name_class = self.registry.__class__.__name__
		mapping = get_fields_mapping(name_class)
		field = {}
		for key, value in mapping.items():
			if hasattr(self.registry, key):
				value_field = getattr(self.registry, key)
				# if isinstance(value_field, datetime.datetime):
					# value_field = get_local_isoformat(value_field)
				field[key] = value_field
		return field
