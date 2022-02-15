''' Módulo para construir la aplicación '''
import os
from os.path import join
import sys
import connexion
from dotenv import load_dotenv
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from .core.base import add_swagger_app
from .core.sentry import create_sentry
from .core.routes import create_routes
from .core.jwt import create_jwt
from .core.mail import create_mail_app
from .core.database import add_migration, add_seeders
from .core.sockets import initalize_socket_app

env_path = join((len(sys.path) > 0 and sys.path[0] + "/" or ""), ".env")
load_dotenv(env_path)

# Sentry
create_sentry()

# Connexion Swager-UI
app = connexion.App(__name__)
flask_app = app.app
flask_app.logger.info(env_path)
config = os.getenv('APP_SETTINGS', "develop")
configs = {
    "develop": "config.DevelopConfig",
    "production": "config.ProductionConfig",
    "staging": "config.StagingConfig"
}
flask_app.config.from_object(configs[config])

db = SQLAlchemy(flask_app)

babel = Babel(flask_app)
create_jwt(flask_app)
flask_app.mail = create_mail_app(flask_app)

add_migration(flask_app, db)
add_seeders(flask_app, db)

add_swagger_app(app, flask_app)
create_routes(flask_app, db)

from .core.blueprint import add_blueprint
from .oauth.routes import create_oauth_app
from .core.injector import create_injector

bp = Blueprint('manage_db', __name__)
add_blueprint(bp, flask_app, db, config)

create_oauth_app(app, db)
create_injector(flask_app)
initalize_socket_app(flask_app)
