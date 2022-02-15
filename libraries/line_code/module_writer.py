""" module_writer.py: """
import re
from libraries.line_code.body_only_field import BodyOnlyField
from libraries.line_code.nothing import Nothing
from libraries.line_code.tag_value import TagValue
from libraries.line_code.body_key_value import BodyKeyValue
from libraries.line_code.input_with_script import InputWithScript
from functions.utils.util import get_model


class ModuleWriter:
    """ Clase ModuleWriter """

    def __init__(self, module):
        self.module = module
        self.lines = None

    def get_lines(self):  # pylint: disable=too-many-locals
        """ get_lines method """

        input_api = self.module.input_api
        input_api.set_inputs()

        path_lines = []
        for input_ in input_api.path_inputs:
            path_lines.append(
                InputWithScript('path', [
                    BodyKeyValue('type', input_.type),
                    BodyKeyValue('required', 'true'),
                    BodyKeyValue('name', input_.field_name),
                ])
            )
        query_lines = []
        for input_ in input_api.query_inputs:
            default_value = []
            if input_.default is not None:
                default_value.append(
                    BodyKeyValue('default', str(input_.default)),
                )
            input_.get_structure()
            query_lines.append(
                InputWithScript('query', [
                    BodyKeyValue('type', input_.type),
                    BodyKeyValue('required', str(input_.required).lower()),
                    BodyKeyValue('name', input_.field_name),
                    *default_value
                ])
            )

        required_body = []
        body_lines = []
        for input_ in input_api.body_inputs:
            body_lines.append(
                self.lines_of_field(input_)
            )
            if input_.config.get('required', True):
                required_body.append(
                    TagValue(input_.field_name)
                )

        part_required_body = []
        if len(required_body) > 0:
            part_required_body.append(
                BodyOnlyField('required', required_body)
            )

        part_body = []
        if len(body_lines) > 0:
            part_body.append(
                InputWithScript('body', [
                    BodyKeyValue('name', 'body'),
                    BodyKeyValue('required', 'true'),
                    BodyOnlyField('schema', [
                        BodyKeyValue('type', 'object'),
                        *part_required_body,
                        BodyOnlyField('properties', [
                            *body_lines
                        ])
                    ])
                ]),
            )

        response_api = self.module.response_api
        response_api.set_response()
        handler = response_api.__dict__['handler']
        fields_mapping = self.get_fields_mapping(response_api.model_name)
        response_part = []
        response_lines_part = []
        for part in handler.__dict__['parts']:
            response_lines_part = [
                *response_lines_part,
                *self.lines_of_response(part, fields_mapping)
            ]

        if len(response_lines_part) > 0:
            response_part.append(
                BodyOnlyField('properties', [
                    *response_lines_part
                ])
            )

        self.lines = Nothing(input_api.type_request.lower(), lines=[
            BodyOnlyField('tags', [
                TagValue(input_api.tag)
            ]),
            BodyKeyValue('operationId', 'modules.{}_{}.{}'.format(
                input_api.version.replace('.', '_'), input_api.module_name, input_api.api_name
            )),
            BodyKeyValue('description', input_api.description),
            BodyOnlyField('parameters', [
                InputWithScript('header', [
                    BodyKeyValue('name', 'Authorization'),
                    BodyKeyValue('description', 'an authorization header'),
                    BodyKeyValue('required', 'true'),
                    BodyKeyValue('type', 'string'),
                ]),
                *path_lines,
                *query_lines,
                *part_body
            ]),
            BodyOnlyField('responses', [
                BodyOnlyField('"{}"'.format(input_api.type_response), [
                    BodyKeyValue('description', 'Successfully output'),
                    BodyOnlyField('schema', [
                        BodyKeyValue('type', 'object'),
                        BodyOnlyField('properties', [
                            BodyKeyValue('errors', '{ type: boolean }'),
                            BodyKeyValue('message', '{ type: string }'),
                            BodyOnlyField('result', [
                                BodyKeyValue('type', 'array'),
                                BodyOnlyField('items', [
                                    BodyKeyValue('type', 'object'),
                                    *response_part
                                ])
                            ]),
                            BodyKeyValue('pagination', '{ type: boolean }')
                        ])
                    ])
                ]),
                BodyOnlyField('"400"', [
                    BodyKeyValue('description', 'Error output'),
                    BodyOnlyField('schema', [
                        BodyKeyValue('type', 'object'),
                        BodyOnlyField('properties', [
                            BodyOnlyField('errors', [
                                BodyKeyValue('type', 'array'),
                                BodyOnlyField('items', [
                                    BodyKeyValue('type', 'object'),
                                    BodyOnlyField('properties', [
                                        BodyKeyValue('field', '{ type: string }'),
                                        BodyKeyValue('message', '{ type: string }'),
                                        BodyOnlyField('extra', [
                                            BodyKeyValue('type', 'object'),
                                            BodyOnlyField('properties', [
                                                BodyKeyValue('of_field', '{ type: string }'),
                                                BodyKeyValue('index', '{ type: integer }')
                                            ])
                                        ])
                                    ])
                                ])
                            ]),
                            BodyKeyValue('message', '{ type: string }'),
                            BodyKeyValue('result', '{ type: boolean }'),
                            BodyKeyValue('pagination', '{ type: boolean }')
                        ])
                    ])
                ]),
            ])
        ])

        return self.lines.get_text()

    def lines_of_field(self, field):  # pylint: disable=too-many-return-statements
        """ lines_of_field method """
        if field.type == 'boolean':
            return BodyKeyValue(field.field_name, '{} type: {} {}'.format('{', 'boolean', '}'))
        if field.type == 'integer':
            return BodyKeyValue(field.field_name, '{} type: {} {}'.format('{', 'integer', '}'))
        if field.type == 'number':
            return BodyKeyValue(field.field_name, '{ type: number, format: double }')
        if field.type == 'string':
            return BodyKeyValue(field.field_name, '{} type: {} {}'.format('{', 'string', '}'))
        if field.type == 'dict':
            childs = []
            for child in field.inputs:
                childs.append(self.lines_of_field(child))
            return BodyOnlyField(field.field_name, [
                BodyKeyValue('type', 'object'),
                BodyOnlyField('properties', [
                    *childs
                ])
            ])
        if field.type == 'list_dicts':
            childs = []
            for child in field.inputs:
                childs.append(self.lines_of_field(child))
            return BodyOnlyField(field.field_name, [
                BodyKeyValue('type', 'array'),
                BodyOnlyField('items', [
                    BodyKeyValue('type', 'object'),
                    BodyOnlyField('properties', [
                        *childs
                    ])
                ])
            ])
        if field.type == 'list_integers':
            return BodyOnlyField(field.field_name, [
                BodyKeyValue('type', 'array'),
                BodyKeyValue('items', '{ type: integer }')
            ])
        if field.type == 'list_strings':
            return BodyOnlyField(field.field_name, [
                BodyKeyValue('type', 'array'),
                BodyKeyValue('items', '{ type: string }')
            ])
        return None

    def lines_of_response(self, response, fields_mapping):
        """ lines_of_response method """
        type_ = response.__class__.__name__
        if type_ == 'ModelField':
            if fields_mapping[response.field_name] == 'DateTime':
                return [BodyKeyValue(response.field_name, '{ type: string }')]
            if fields_mapping[response.field_name] == 'Boolean':
                return [BodyKeyValue(response.field_name, '{ type: boolean }')]
            if fields_mapping[response.field_name] == 'Integer':
                return [BodyKeyValue(response.field_name, '{ type: integer }')]
            if fields_mapping[response.field_name] == 'String':
                return [BodyKeyValue(response.field_name, '{ type: string }')]
        elif type_ == 'ModelFields':
            response = []
            for key, value in fields_mapping.items():
                if value == 'DateTime':
                    response.append(BodyKeyValue(key, '{ type: string }'))
                elif value == 'Boolean':
                    response.append(BodyKeyValue(key, '{ type: boolean }'))
                elif value == 'Integer':
                    response.append(BodyKeyValue(key, '{ type: integer }'))
                elif value == 'String':
                    response.append(BodyKeyValue(key, '{ type: string }'))
            return response
        return None

    def get_fields_mapping(self, model_name):
        """ get_fields_mapping method """
        model = get_model(model_name)
        constraints = list(model.__dict__['__table__'].__dict__['constraints'])
        constraint = None
        for key in constraints:
            if key.__class__.__name__ == 'CheckConstraint':
                constraint = key

        # pylint: disable=line-too-long
        fields_mapping = re.findall(r"Column\(\'([a-zA-Z_]*)\', ([a-zA-Z]*)\([a-zA-Z=0-9]*\),", str(constraint))

        return dict(fields_mapping)
