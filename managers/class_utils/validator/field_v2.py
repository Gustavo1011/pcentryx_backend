class FieldV2():
	def __init__(self, name):
		self.name = name
		self.list_data = []

	def get_value(self, global_data, parent_data):
		string_parts = self.name.split('.')
		value = None
		for index, string_part in enumerate(string_parts):
			name_part = string_part
			is_function = False
			if string_part[-2:len(string_part)] == '()':
				name_part = string_part[0:-2]
				is_function = True
			if value == None:
				is_in_list_data = False
				for element_data in self.list_data:
					if name_part in element_data:
						value = element_data.get(name_part)
						is_in_list_data = True
						break
				if is_in_list_data is False:
					if name_part in parent_data:
						value = parent_data.get(name_part)
					else:
						value = global_data.get(name_part)
			else:
				if isinstance(value, dict):
					value = value.get(name_part)
				else:
					value = getattr(value, name_part)
			if is_function is True:
				value = value()
		return value