from sqlalchemy import or_
from functions.general.general import accent
from managers.utils.manager_general import unaccent
from functions.utils.util import remove_extra_spaces

class FilterSearch():
    def __init__(self, fields=[], value=None):
        self.fields = fields
        self.value = value

    def translate(self, vars_):
        if self.value is None or self.value == '' or len(self.fields) == 0:
            return []
        filter_array = []
        for field in self.fields:
            value = accent(remove_extra_spaces(self.value))
            filter_array.append(unaccent(vars_[field]).ilike('%{}%'.format(value)))
        if len(filter_array) > 1:
            return [or_(*filter_array)]
        return filter_array
