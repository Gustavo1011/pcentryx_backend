class WriterModule():
    def __init__(self, module_name, api_name, version):
        self.module_name = module_name
        self.api_name = api_name
        self.version = version

    def writer(self):
        import os
        def use_dir(route):
            try:
                os.stat(route)
            except:
                os.mkdir(route)
        def convert_to_camel_case(value):
            strings = value.split('_')
            return ''.join(word.capitalize() for word in strings)
        module_name = self.module_name
        api_name = self.api_name
        version = self.version
        dir_name_module = "apis/{}_{}".format(version.replace('.', '_'), module_name)
        use_dir(dir_name_module)
        dir_name_api = '{}/{}'.format(dir_name_module, api_name)
        use_dir(dir_name_api)
        file = open(dir_name_api + "/flow.py", "w")
        file.write('""" Define el flujo para el API {} """\n\n'.format(api_name))
        file.write('class {}Flow:\n'.format(convert_to_camel_case(api_name)))
        file.write('    """ Clase para definir el flujo del API {} """\n'.format(api_name))
        file.write('    def __init__(self):\n')
        file.write('        """ Constructor de la clase """\n')
        file.write('        self.data = None\n\n')
        file.write('    def action(self):\n')
        file.write('        """ Función que define el flujo del API """\n')
        file.write('        return dict()\n')
        file.close()

        file = open(dir_name_api + "/input.py", "w")
        file.write('""" Define las entradas del API {} """\n'.format(api_name))
        file.write('from managers.class_utils.input.input_api import InputAPI\n\n'.format(api_name))
        file.write('class {}Input(InputAPI):\n'.format(convert_to_camel_case(api_name)))
        file.write('    """ Clase para definir las entradas del API {} """\n'.format(api_name))
        file.write('    def __init__(self):\n')
        file.write('        """ Constructor de la clase """\n')
        file.write('        super().__init__()\n')
        file.write('        self.module_name = "{}"\n'.format(module_name))
        file.write('        self.tag = "{} Management"\n'.format(convert_to_camel_case(module_name)))
        file.write('        self.api_name = "{}"\n'.format(api_name))
        file.write('        self.version = "{}"\n'.format(version))
        file.write('        self.route = "brands/{brand_id} FALTA LLENAR"\n')
        file.write('        self.type_request = "GET, POST, PUT, DELETE FALTA LLENAR"\n')
        file.write('        self.type_response = "200, 201 FALTA LLENAR"\n')
        file.write('        self.description = "FALTA LLENAR"\n\n')
        file.write('    def set_inputs(self):\n')
        file.write('        """ Función que define las entradas del API """\n')
        file.write('        self.set_path([])\n')
        file.write('        self.set_query([])\n')
        file.write('        self.set_body([])\n')
        file.close()

        file = open(dir_name_api + "/response.py", "w")
        file.write('""" Define la respuesta del API {} """\n'.format(api_name))
        file.write('from managers.class_utils.response.response_api import ResponseAPI\n'.format(api_name))
        file.write('from managers.class_utils.response.model_fields import ModelFields\n\n'.format(api_name))
        file.write('class {}Response(ResponseAPI):\n'.format(convert_to_camel_case(api_name)))
        file.write('    """ Clase para definir la salida del API {} """\n'.format(api_name))
        file.write('    def __init__(self):\n')
        file.write('        """ Constructor de la clase """\n')
        file.write('        super().__init__()\n')
        file.write('        self.model_name = "Brand FALTA LLENAR"\n\n')
        file.write('    def set_response(self):\n')
        file.write('        """ Función que define la salida del API """\n')
        file.write('        self.set_structure([\n')
        file.write('            ModelFields()\n')
        file.write('        ])\n')
        file.close()

        file = open(dir_name_api + "/validator.py", "w")
        file.write('""" Define las validaciones del API {} """\n'.format(api_name))
        file.write('from managers.class_utils.validator.validator_api import ValidatorAPI\n\n')
        file.write('class {}Validator(ValidatorAPI):\n'.format(convert_to_camel_case(api_name)))
        file.write('    """ Clase para definir las validaciones del API {} """\n'.format(api_name))
        file.write('    def __init__(self):\n')
        file.write('        """ Constructor de la clase """\n')
        file.write('        super().__init__()\n\n')
        file.write('    def validate_api(self):\n')
        file.write('        """ Función que define las validaciones del API """\n')
        file.write('        self.set_validators([])\n')
        file.close()

        file = open(dir_name_api + "/module.py", "w")
        file.write('""" Define el módulo del API {} """\n'.format(api_name))
        file.write('from apis.{}_{}.{}.input import {}Input\n'.format(version.replace('.', '_'), module_name, api_name, convert_to_camel_case(api_name)))
        file.write('from apis.{}_{}.{}.validator import {}Validator\n'.format(version.replace('.', '_'), module_name, api_name, convert_to_camel_case(api_name)))
        file.write('from apis.{}_{}.{}.flow import {}Flow\n'.format(version.replace('.', '_'), module_name, api_name, convert_to_camel_case(api_name)))
        file.write('from apis.{}_{}.{}.response import {}Response\n'.format(version.replace('.', '_'), module_name, api_name, convert_to_camel_case(api_name)))
        file.write('from managers.class_utils.module.module_api import ModuleAPI\n\n')
        file.write('class {}Module(ModuleAPI):\n'.format(convert_to_camel_case(api_name)))
        file.write('    """ Clase para definir el módulo del API {} """\n'.format(api_name))
        file.write('    def __init__(self, data):\n')
        file.write('        """ Constructor de la clase """\n')
        file.write('        super().__init__()\n')
        file.write('        self.data = data\n')
        file.write('        self.input_api = {}Input()\n'.format(convert_to_camel_case(api_name)))
        file.write('        self.validator_api = {}Validator()\n'.format(convert_to_camel_case(api_name)))
        file.write('        self.flow_api = {}Flow()\n'.format(convert_to_camel_case(api_name)))
        file.write('        self.response_api = {}Response()\n'.format(convert_to_camel_case(api_name)))
        file.close()
