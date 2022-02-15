''' Módulo para la configuración de JWT '''
import os
from flask_jwt_extended import JWTManager

def create_jwt(app):
    ''' Crear configuración de JWT '''
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_TIME_TOKEN', '900'))
    JWTManager(app)
