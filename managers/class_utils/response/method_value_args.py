from managers.class_utils.response.response_field import ResponseField

class MethodValueArgs(ResponseField):
    def __init__(self, method_name, key_name, args = None):
        self.method_name = method_name
        self.key_name = key_name
        self.registry = None
        self.args = args

    def get_field(self):
        field = {}
        if self.args is None:
            self.args = []
        if hasattr(self.registry, self.method_name):
            value_field = getattr(self.registry, self.method_name)
            field[self.key_name] = value_field(*self.args)
        return field
