"""
worker.py: Worker RQ file
"""
import os
from dotenv import load_dotenv # pylint: disable=import-error

import redis # pylint: disable=import-error
from rq import Worker, Queue, Connection # pylint: disable=import-error

load_dotenv()

LISTEN = [
    'default',
    'model_base',
    'stock_movement'
]

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
CONNECTION = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

if __name__ == '__main__':
    with Connection(CONNECTION):
        # pylint: disable=invalid-name
        worker = Worker(list(map(Queue, LISTEN)))
        worker.work()
