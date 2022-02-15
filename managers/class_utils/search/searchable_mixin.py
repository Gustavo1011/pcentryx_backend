'''
searchable_mixin.py: File to manage searching
'''

from managers.class_utils.search.searchable import sort_by, paginate, set_filters

class SearchableMixin():
    ''''Class to manage searching'''

    @classmethod
    def search(cls, filters, limit=None, page=None, sort=None, order=None):
        '''
        Search is a method to use from a class instance to do searches
        It can receive null arguments or leave them empty
        '''
        query = set_filters(cls, filters)
        count = False
        if sort:
            query = sort_by(cls, query, sort, order)
        if limit:
            query = paginate(query, page, limit)
            count = len(query)
        return query, count
