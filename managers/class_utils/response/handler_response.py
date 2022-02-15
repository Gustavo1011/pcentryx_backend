class HandlerResponse():
    '''Clase lógica handler response'''
    def __init__(self, value):
        self.value = value
        self.parts = []
        self.response = {}

    def get_response(self):
        if isinstance(self.value, list):
            self.set_dicts()
        else:
            self.set_dict()
        return self.response

    def set_dicts(self):
        self.response = []
        for part_value in self.value:
            self.response_dict = {}
            for part in self.parts:
                part.registry = part_value
                self.response_dict.update(part.get_field())
            self.response.append(self.response_dict)

    def set_dict(self):
        self.response = {}
        for part in self.parts:
            part.registry = self.value
            self.response.update(part.get_field())
