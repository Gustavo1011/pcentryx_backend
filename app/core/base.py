''' Módulo para la configuración de aplicación base '''
from typing import Any, Dict
from pathlib import Path
from connexion.resolver import RestyResolver
from flask_cors import CORS
from libraries.swagger_validator import SwaggerValidator
import prance # pylint: disable=import-error
from flask import request

def add_swagger_app(app, flask_app):
    ''' Añade la documentación Swagger a la aplicación '''
    flask_app.url_map.strict_slashes = False
    app.add_api(
        get_bundled_specs(),
        resolver=RestyResolver('modules'),
        validator_map={"body": SwaggerValidator}
    )
    CORS(flask_app)

    @flask_app.before_request
    def connexion_flask_before_request():
        if request.headers.get('From') == "test":
            flask_app.config['ELASTICSEARCH_REFRESH'] = 'false'

    @flask_app.after_request
    def connexion_flask_after_request(response):
        if request.headers.get('From') == "test":
            flask_app.config['ELASTICSEARCH_REFRESH'] = 'wait_for'
        return response

def get_bundled_specs() -> Dict[str, Any]:
    ''' Obtiene la especificación de archivo de Swagger '''
    parser = prance.ResolvingParser(str(Path("swagger/erp.yaml").absolute()),
                                    lazy=True, strict=True)
    parser.parse()
    return parser.specification
