class WriterErpYaml():
    def __init__(self, tags, paths):
        self.tags = tags
        self.paths = paths

    def write(self):
        from libraries.line_code.nothing import Nothing
        from libraries.line_code.body_only_field import BodyOnlyField
        from libraries.line_code.body_key_value import BodyKeyValue

        tags_lines = []
        for tag in self.tags:
            tags_lines.append(BodyKeyValue('- name', tag))

        path_lines = []
        for clave, valor in self.paths.items():
            if valor['type'] == 'antiguo':
                path_lines.append(BodyOnlyField(clave, [
                    BodyKeyValue('$ref', 'erp_modules/{}'.format(valor['value']))
                ]))
            elif valor['type'] == 'antiguo_especial':
                path_lines.append(
                    BodyOnlyField(clave, [
                        BodyOnlyField(valor['value'], [
                            BodyKeyValue('$ref', valor['other_value'])
                        ])
                    ])
                )
            else:
                method_lines = []
                for clave_2, valor_2 in valor['methods'].items():
                    method_lines.append(BodyOnlyField(clave_2, [
                        BodyKeyValue('$ref', 'erp_modules/{}'.format(valor_2))
                    ]))
                path_lines.append(BodyOnlyField(clave, [
                    *method_lines
                ]))

        lines = Nothing('test', lines=[
            BodyKeyValue('swagger', '"2.0"'),
            BodyOnlyField('info', [
                BodyKeyValue('title', '"ERP API"'),
                BodyKeyValue('version', '"1.0"')
            ]),
            BodyKeyValue('basePath', '/erp'),
            BodyOnlyField('tags'),
            *tags_lines,
            BodyOnlyField('paths', [
                *path_lines
            ]),
        ])
        file = open("swagger/erp.yaml", "w")
        file.write(lines.get_text())
        file.close()