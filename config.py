"""
Módulo de configuración de variables de ambiente
"""
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:  # pylint: disable=too-few-public-methods
    """Configuration class"""
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', "postgres_unknown:5432")
    POSTGRES_DB = os.getenv('POSTGRES_DB', "postgres_unknown")
    POSTGRES_USER = os.getenv('POSTGRES_USER', "postgres_unknown")
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', "postgres_unknown")
    db_url = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER,
        pw=POSTGRES_PASSWORD,
        url=POSTGRES_HOST,
        db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    ERP_AWS_ACCESS_KEY_ID = os.getenv('ERP_AWS_ACCESS_KEY_ID', "")
    ERP_AWS_SECRET_ACCESS_KEY = os.getenv('ERP_AWS_SECRET_ACCESS_KEY', "")
    ERP_AWS_DEFAULT_REGION = os.getenv('ERP_AWS_DEFAULT_REGION', "")
    ERP_AWS_BUCKET_NAME = os.getenv('ERP_AWS_BUCKET_NAME', "")

    LANGUAGES = {
        'en': 'English',
        'es': 'Español'
    }
    BABEL_DEFAULT_LOCALE = 'es'

class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """Class for production mode configuration"""
    ELASTICSEARCH_REFRESH = 'wait_for'
class StagingConfig(Config):  # pylint: disable=too-few-public-methods
    """Class for staging mode configuration"""
    ELASTICSEARCH_REFRESH = 'wait_for'
class DevelopConfig(Config):  # pylint: disable=too-few-public-methods
    """Class for development mode configuration"""
    DEVELOPMENT = True
    ELASTICSEARCH_REFRESH = 'wait_for'
