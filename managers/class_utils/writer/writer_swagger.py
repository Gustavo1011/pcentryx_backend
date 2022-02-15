class WriterSwagger():
    def __init__(self, module_name, api_name, version):
        self.module_name = module_name
        self.api_name = api_name
        self.version = version

    def write(self):
        import os
        from libraries.line_code.module_writer import ModuleWriter
        def use_dir(route):
            try:
                os.stat(route)
            except:
                os.mkdir(route)

        def convert_to_camel_case(value):
            strings = value.split('_')
            return ''.join(word.capitalize() for word in strings)

        dir_name = 'swagger/erp_modules/{}_{}'.format(self.version.replace('.', '_'), self.module_name)
        use_dir(dir_name)

        module_route = 'apis.{}_{}.{}.module'.format(self.version.replace('.', '_'), self.module_name, self.api_name)
        class_name = convert_to_camel_case(self.api_name) + 'Module'
        entity_module = __import__(module_route, fromlist=[class_name])
        module_class = getattr(entity_module, class_name)
        module = module_class({})
        writer = ModuleWriter(module)

        file = open("{}/{}.yaml".format(dir_name, self.api_name), "w")
        file.write(writer.get_lines())
        file.close()
