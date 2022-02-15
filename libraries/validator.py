"""
validator.py: File to manage validation response messages
"""
import copy
import cerberus
from cerberus import errors as cerrors
from flask_babel import lazy_gettext

class CustomErrorHandler(cerberus.errors.BasicErrorHandler):
    """Defined class to manage validation response messages"""
    messages = cerberus.errors.BasicErrorHandler.messages.copy()
    messages.update({
        cerrors.REQUIRED_FIELD.code: lazy_gettext("Required field"),
        cerrors.UNKNOWN_FIELD.code: lazy_gettext("Unknown field"),
        cerrors.DEPENDENCIES_FIELD.code: lazy_gettext("Field '{0}' is required"),
        cerrors.DEPENDENCIES_FIELD_VALUE.code: lazy_gettext(
            "Depends on these values: {constraint}"
        ),
        cerrors.EXCLUDES_FIELD.code: lazy_gettext("{0} must not be present with '{field}'"),

        cerrors.EMPTY_NOT_ALLOWED.code: lazy_gettext("Field should not be empty"),
        cerrors.NOT_NULLABLE.code: lazy_gettext("Field should not be empty"),
        cerrors.BAD_TYPE.code: lazy_gettext("Must be of {constraint} type"),
        cerrors.ITEMS_LENGTH.code: lazy_gettext("Length of list should be {constraint}, it is {0}"),
        cerrors.MIN_LENGTH.code: lazy_gettext("Min length is {constraint}"),
        cerrors.MAX_LENGTH.code: lazy_gettext("Max length is {constraint}"),

        # cerrors.REGEX_MISMATCH.code: lazy_gettext("Value does not match regex '{constraint}'"),
        cerrors.REGEX_MISMATCH.code: lazy_gettext("Invalid value format"),
        cerrors.MIN_VALUE.code: lazy_gettext("Min value is {constraint}"),
        cerrors.MAX_VALUE.code: lazy_gettext("Max value is {constraint}"),
        cerrors.UNALLOWED_VALUE.code: lazy_gettext("Unallowed value {value}"),
        cerrors.UNALLOWED_VALUES.code: lazy_gettext("Unallowed values {0}"),
        cerrors.FORBIDDEN_VALUE.code: lazy_gettext("Unallowed value {value}"),
        cerrors.FORBIDDEN_VALUES.code: lazy_gettext("Unallowed values {0}"),

        cerrors.COERCION_FAILED.code: lazy_gettext("Field '{field}' cannot be coerced"),
        cerrors.RENAMING_FAILED.code: lazy_gettext("Field '{field}' cannot be renamed"),
        cerrors.READONLY_FIELD.code: lazy_gettext("Field is read-only"),
        cerrors.SETTING_DEFAULT_FAILED.code: lazy_gettext(
            "Default value for '{field}' cannot be set: {0}"
        ),

        cerrors.MAPPING_SCHEMA.code: lazy_gettext("Mapping doesn't validate subschema: {0}"),
        cerrors.SEQUENCE_SCHEMA.code: lazy_gettext(
            "One or more sequence-items don't validate: {0}"
        ),
        cerrors.KEYSCHEMA.code: lazy_gettext(
            "One or more properties of a mapping  don't validate: {0}"
        ),
        cerrors.VALUESCHEMA.code: lazy_gettext(
            "One or more values in a mapping don't validate: {0}"
        ),

        cerrors.NONEOF.code: lazy_gettext("One or more definitions validate"),
        cerrors.ONEOF.code: lazy_gettext("None or more than one rule validate"),
        cerrors.ANYOF.code: lazy_gettext("No definitions validate"),
        cerrors.ALLOF.code: lazy_gettext("One or more definitions don't validate"),
    })

    def __init__(self, tree=None, custom_messages=None):
        """Initial function"""
        super().__init__(tree)
        self.custom_messages = custom_messages or {}

    def format_message(self, field, error):
        """Visualize the text in a better way"""
        tmp = self.custom_messages
        for key, value in enumerate(error.schema_path):
            try:
                tmp = tmp[value]
            except KeyError:
                if key == len(error.schema_path) - 1 and 'any' in tmp:
                    return tmp['any']
                return super().format_message(field, error)
        if isinstance(tmp, dict):
            return super().format_message(field, error)
        return tmp

class Validator(cerberus.Validator):
    """Defined class to manage the validation"""

    def __init__(self, *args, **kwargs):
        """Initial function"""
        if args:
            if 'schema' in kwargs:
                raise TypeError("got multiple values for argument 'schema'")
            schema = args[0]
        else:
            schema = kwargs.pop('schema')

        if isinstance(schema, dict):
            schema = copy.deepcopy(schema)
            self.populate_custom_messages(schema)
            args = [schema] + list(args[1:])

        kwargs['error_handler'] = CustomErrorHandler(custom_messages=self.custom_messages)
        if 'purge_unknown' not in kwargs:
            kwargs['purge_unknown'] = True
        super().__init__(*args, **kwargs)
        self.custom_messages = {}
        self._allowed_func_caches = {}

    def populate_custom_messages(self, schema):
        """Custom messages"""
        self.custom_messages = {}
        queue = [(schema, self.custom_messages)]
        while queue:
            item, msgs = queue.pop()
            if 'error_messages' in item:
                if not isinstance(item['error_messages'], dict):
                    raise Exception('Type of instance not passed\nType of instance should be dict')
                msgs.update(item.pop('error_messages'))
            for key, value in item.items():
                if isinstance(value, dict):
                    msgs[key] = {}
                    queue.append((value, msgs[key]))
