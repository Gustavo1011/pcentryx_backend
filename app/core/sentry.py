''' Módulo para la configuración de sentry '''

import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.rq import RqIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.redis import RedisIntegration

def create_sentry():
    ''' Incorpora sentry a la aplicación '''
    if os.getenv('SENTRY', "True") == 'True':
        sentry_sdk.init(
            dsn=os.getenv(
                'SENTRY_URL',
                "https://9804175bb7ee4269bf858712b9d95b8d@o444243.ingest.sentry.io/5418920"
            ),
            integrations=[
                FlaskIntegration(),
                SqlalchemyIntegration(),
                RqIntegration(),
                RedisIntegration()
            ],
            traces_sample_rate=1.0
        )
