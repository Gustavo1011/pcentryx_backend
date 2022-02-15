from libraries.response import entity_response
import math


class ModuleAPI:
    def __init__(self):
        self.data = None
        self.input_api = None
        self.validator_api = None
        self.flow_api = None
        self.response_api = None
        self.is_searchable_api = False

    def use_api(self):
        self.input_api.set_inputs()
        data = dict(self.data)
        for query_input in self.input_api.query_inputs:
            if query_input.type == 'integer' and query_input.field_name in data:
                data[query_input.field_name] = int(data[query_input.field_name])
            elif query_input.type == 'boolean' and query_input.field_name in data:
                data[query_input.field_name] = data[query_input.field_name] == 'true'
        self.data = data
        self.validator_api.module = self
        self.validator_api.data = self.data
        self.validator_api.validate()
        if hasattr(self.validator_api, 'response_object'):
            flow_response_object = self.validator_api.response_object
        else:
            flow_response_object = {}
        if self.validator_api.has_response_error():
            return {
                "response": flow_response_object,
                **self.validator_api.response_error
            }, 400
        self.flow_api.data = self.data
        response_flow = self.flow_api.action()
        if self.response_api is None:
            return response_flow, 200
        self.response_api.value = response_flow
        self.response_api.data = self.data
        response = self.response_api.get_response()

        parts_version = self.input_api.version[1:].split('.')
        if int(parts_version[0]) > 5 or (int(parts_version[0]) == 5 and int(parts_version[1]) > 0):
            pagination_dict = {'pagination': None}
            if self.input_api.type_request.lower() in ['get', 'post'] and \
            self.is_searchable_api and 'page' in self.data and \
            'limit' in self.data:
                pagination_dict['pagination'] = {
                    'page': self.data['page'],
                    'pages': math.ceil(self.flow_api.total / self.data['limit']),
                    'total': self.flow_api.total
                }
            return {
                "result": response,
                **pagination_dict
            }, int(self.input_api.type_response)

        if self.input_api.type_request.lower() == 'get':
            if self.is_searchable_api and 'page' in self.data and 'limit' in self.data:
                return entity_response(
                    200,
                    message="The search has been successful",
                    result=response,
                    pagination={
                        'page': self.data['page'],
                        'pages': math.ceil(self.flow_api.total / self.data['limit']),
                        'total': self.flow_api.total
                    }
                )

            return entity_response(
                200,
                message="The search has been successful",
                result=response
            )
        elif self.input_api.type_request.lower() == 'delete':
            return entity_response(200, message="The delete has been successful")
        else:
            return entity_response(
                201,
                message="Registration has been successful",
                result=response
            )
