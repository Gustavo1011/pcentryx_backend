'''
http_requests.py: File to encapsulate requests that we use in our tests
'''

import requests
import os

class HttpRequest:
    '''
    HttpRequest is a class to encapsulate requests that we use in our tests 
    .. versionadded:: 1.0
    '''
    
    def __init__(self, context, path):
        self.context = context
        self.path = path
        self.headers = {
            'content_type': 'application/json',
            'From': 'test',
            'Authorization': self.context.key_login
        }

    def post(self):
        '''Return a post request'''
        return requests.post(
            url=os.getenv('BASE_URL', "") + self.path,
            json=self.context.data,
            headers=self.headers
        )

    def put(self):
        '''Return a put request'''
        return requests.put(
            url=os.getenv('BASE_URL', "") + self.path,
            json=self.context.data if hasattr(self.context, 'data') else None,
            headers=self.headers
        )

    def get(self):
        '''Return a get request'''
        return requests.get(
            url=os.getenv('BASE_URL', "") + self.path,
            headers=self.headers
        )

    def delete(self):
        '''Return a delete request'''
        return requests.delete(
            url=os.getenv('BASE_URL', "") + self.path,
            headers=self.headers
        )
