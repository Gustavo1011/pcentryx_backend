
class FilterValue():
	def __init__(self, alias, value):
		if isinstance(value, bool):
			self.value = str(value).lower()
		else:
			self.value = value
		self.alias = alias

	def translate(self, vars_):
		return [vars_[self.alias] == self.value] 