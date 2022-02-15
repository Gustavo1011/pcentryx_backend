'''
call_api_search.py: File to manage the path in search's api
'''

from managers.class_utils.manage_tests.http_requests import HttpRequest

class CallAPISearch(HttpRequest):
    '''
    CallAPISearch is a class to manage the path in search's api
    .. Inherits: inherits from class HttpRequest to use the method get()
    .. versionadded:: 1.0
    '''

    def __init__(self, context, base_path, queries=[]):
        HttpRequest.__init__(self, context, base_path)
        self.context = context
        self.base_path = base_path
        self.queries = queries

    def get_path(self):
        '''Get the path with all queries'''
        self.path = self.base_path + '?'
        for query in self.queries:
            if getattr(self.context, query):
                self.path += '&{}={}'.format(query, getattr(self.context, query))
