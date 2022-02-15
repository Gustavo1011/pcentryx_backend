class WriterModuleSwagger():
    def __init__(self, module_name, version):
        self.module_name = module_name
        self.version = version

    def write(self):
        import glob

        def convert_to_camel_case(value):
            strings = value.split('_')
            return ''.join(word.capitalize() for word in strings)

        targetPattern = r"apis/{}_{}/*/module.py".format(self.version.replace('.', '_'), self.module_name)
        rutas = glob.glob(targetPattern)
        api_names = []
        for ruta in rutas:
            api_names.append(ruta.split('/')[-2])

        file = open("modules/{}_{}.py".format(self.version.replace('.', '_'), self.module_name), "w")
        file.write('"""\n')
        file.write('{}_{}.py: {} module\n'.format(self.version.replace('.', '_'), self.module_name, self.module_name.capitalize()))
        file.write('"""\n')
        file.write('from flask_jwt_extended import jwt_required\n')
        file.write('from functions.utils.request_type import get_data\n')
        for api_name_u in api_names:
            file.write('from apis.{}_{}.{}.module import {}Module\n'.format(self.version.replace('.', '_'), self.module_name, api_name_u, convert_to_camel_case(api_name_u)))

        for api_name_u in api_names:
            file.write('\n')
            file.write('@jwt_required\n')
            file.write('def {}(**kwargs):\n'.format(api_name_u))
            file.write('    """Function for {}"""\n'.format(api_name_u.replace('_', ' ')))
            file.write('    module = {}Module(get_data())\n'.format(convert_to_camel_case(api_name_u)))
            file.write('    return module.use_api()\n')
        file.close()
