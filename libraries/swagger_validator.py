''' Librería para personalizar respuestas de validación de swagger '''

from connexion import decorators
from connexion.lifecycle import ConnexionResponse
from jsonschema import ValidationError
from flask_babel import gettext

class SwaggerValidator(decorators.validation.RequestBodyValidator):
    """
    This class overrides the default connexion RequestBodyValidator
    so that it returns the complete string representation of the
    error, rather than just returning the error message.

    For more information:
        - https://github.com/zalando/connexion/issues/558
        - https://connexion.readthedocs.io/en/latest/request.html
    """
    def validate_schema(self, data, url):
        # pylint: disable=undefined-variable
        if self.is_null_value_valid and is_null(data):
            return None
        try:
            self.validator.validate(data)
        except ValidationError as exception:
            problem_response = {
                'errors': True,
                'message': exception.message,
                'result': False,
                'pagination': False
            }

            count = len(list(exception.path))

            if count == 0:
                finds = exception.message.split("'")[1::2]
                field = finds[0]
                problem_response = {
                    'errors': [{
                        'field': field,
                        'message': gettext("Required field"),
                        'extra': False
                    }],
                    'message': gettext("Invalid request"),
                    'result': False,
                    'pagination': False
                }
            if count == 1:
                exceptions = list(exception.path)
                field = exceptions[0]
                problem_response = {
                    'errors': [{
                        'field': field,
                        'message': gettext("Invalid value format"),
                        'extra': False
                    }],
                    'message': gettext("Invalid request"),
                    'result': False,
                    'pagination': False
                }
            if count == 2:
                exceptions = list(exception.path)
                index = exceptions[1]
                field = exceptions[0]
                problem_response = {
                    'errors': [{
                        'field': field,
                        'message': gettext("Invalid value format"),
                        'extra': {
                            'of_field': 'value',
                            'index': index
                        }
                    }],
                    'message': gettext("Invalid request"),
                    'result': False,
                    'pagination': False
                }
            if count == 3:
                exceptions = list(exception.path)
                of_field = exceptions[0]
                index = exceptions[1]
                field = exceptions[2]
                problem_response = {
                    'errors': [{
                        'field': field,
                        'message': gettext("Invalid value format"),
                        'extra': {
                            'of_field': of_field,
                            'index': index
                        }
                    }],
                    'message': gettext("Invalid request"),
                    'result': False,
                    'pagination': False
                }

            mimetype = content_type = 'application/problem+json'
            return ConnexionResponse(400, mimetype, content_type, body=problem_response)
        return None
