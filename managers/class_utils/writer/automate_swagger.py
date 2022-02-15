class AutomateSwagger():
    def __init__(self, module_name, api_name, version):
        self.module_name = module_name
        self.api_name = api_name
        self.version = version

    def write(self):
        import glob

        def convert_to_camel_case(value):
            strings = value.split('_')
            return ''.join(word.capitalize() for word in strings)

        targetPattern = r"apis/*/*/module.py"
        rutas = glob.glob(targetPattern)
        tags = set([
            'User Access',
            'User Maintenance',
            'Notification Maintenance',
            'Brand Management',
            'Product Category Management',
            'Product Subcategory Management',
            'Permission Management',
            'Product Management',
            'Provider Management',
            'Analyst Management',
            'Requisition Management',
            'Global',
            'Requistion Management',
            'Agent Management',
            'Provider Product Relationship',
            'Tracking Number Process',
            'Warehouse Management',
            'Product Prices Management',
            'Document Management',
            'Document History Management',
            'Main Provider Management',
            'Access Management'
        ])
        paths = {
            '/login/': {'type': 'antiguo', 'value': 'users/login.yaml'},
        }
        for ruta in rutas:
            new_ruta = ruta.replace('/', '.').replace('.py', '')
            class_name = convert_to_camel_case(new_ruta.split('.')[-2]) + 'Module'
            entity_module = __import__(new_ruta, fromlist=[class_name])
            module_class = getattr(entity_module, class_name)
            instance_class = module_class({})
            input_api = instance_class.input_api

            path_name = '/{}/{}'.format(input_api.version, input_api.route)
            if path_name in paths:
                if paths[path_name]['type'] == 'antiguo':
                    raise Exception('Existe uno antiguo')
                else:
                    paths[path_name]['methods'][instance_class.input_api.type_request.lower()] = '{}_{}/{}.yaml'.format(input_api.version.replace('.', '_'), input_api.module_name, input_api.api_name)
            else:
                paths[path_name] = {'type': 'nuevo', 'methods': {instance_class.input_api.type_request.lower(): '{}_{}/{}.yaml'.format(input_api.version.replace('.', '_'), input_api.module_name, input_api.api_name)}}

            tags.add(instance_class.input_api.tag)

        from managers.class_utils.writer.writer_module_swagger import WriterModuleSwagger
        from managers.class_utils.writer.writer_swagger import WriterSwagger
        from managers.class_utils.writer.writer_erp_yaml import WriterErpYaml
        writer = WriterModuleSwagger(self.module_name, self.version)
        writer.write()
        writer = WriterSwagger(self.module_name, self.api_name, self.version)
        writer.write()
        writer = WriterErpYaml(tags, paths)
        writer.write()
