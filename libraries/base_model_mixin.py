''' Librería para anexar a modelo de datos con funciones base '''

# import os
# import json
# from flask import current_app
# from redis import Redis # pylint: disable=import-error
# from rq import Queue # pylint: disable=import-error
from app import db
# from libraries.redis_functions import delete_cascade, null_entity
# from libraries.utils import get_model

class BaseModelMixin(): # pylint: disable=too-few-public-methods
    ''' Clase para anexar a modelo de datos con funciones base '''

    no_delete_events = False

    @classmethod
    def after_commit(cls, session): # pylint: disable=too-many-locals
        ''' Función después de enviar commit de db '''
        # pylint: disable=protected-access
        # for obj in session._changes['update']:
        #     if obj.deleted and obj.no_delete_events is False:
        #         class_name = obj.__class__.__name__
        #         for file in os.listdir("models"):
        #             if file not in ["__init__.py", "__pycache__", "oauth2.py"]:
        #                 filename = file.replace(".py", "")
        #                 model_child = get_model(filename, snake=False)
        #                 if hasattr(model_child, '__dependencies__'):
        #                     for dependency in model_child.__dependencies__:
        #                         if dependency[0] == class_name:
        #                             if dependency[2] == 'CASCADE' or \
        #                             dependency[2] == 'NULL_APPLY':
        #                                 if current_app.config['QUEUE_DRIVER'] == "redis":
        #                                     exec_function = delete_cascade \
        #                                         if dependency[2] == 'CASCADE' else null_entity
        #                                     entity = '{filename},{field},{id}'.format(
        #                                         filename=filename,
        #                                         field=dependency[1],
        #                                         id=obj.id
        #                                     )
        #                                     redis_host = current_app.config['REDIS_HOST']
        #                                     redis_port = current_app.config['REDIS_PORT']
        #                                     redis = Redis(host=redis_host, port=redis_port)
        #                                     queue = Queue("model_base", connection=redis)
        #                                     queue.enqueue(exec_function, entity, result_ttl=0)
        #                                 elif current_app.config['QUEUE_DRIVER'] == "aws_lambda":
        #                                     data = {
        #                                         'tablename': model_child.__tablename__,
        #                                         'dependency': dependency[1],
        #                                         'value': obj.id
        #                                     }
        #                                     json_encoded = json.dumps(data)
        #                                     log_message = dependency[2] + " " + json_encoded
        #                                     current_app.logger.info(log_message)

db.event.listen(db.session, 'after_commit', BaseModelMixin.after_commit)
