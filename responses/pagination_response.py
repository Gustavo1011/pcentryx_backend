'''pagination_response.py: File to manage pagination response'''
import math

class PaginationResponse:
    '''Class to manage pagination response'''

    def __init__(self):
        self.pagination = False
        self.total = False
        self.limit = False
        self.page = False

    def update_pagination(self):
        """Entity response to search"""
        self.pagination = {
            'total': self.total,
            'page': self.page,
            'pages': math.ceil(self.total / self.limit)
        }
