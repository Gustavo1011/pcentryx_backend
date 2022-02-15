''' Librería para anexar a modelo de datos con ElasticSearch '''

from app import db
from .searchable import add_to_index, remove_from_index, clear_doc_type, query_index

class SearchableMixin():
    ''' Clase para anexar a modelo de datos con ElasticSearch '''

    cascade_searchable = False

    @classmethod
    def search(cls, queries, offset, limit, sort, order=None):
        ''' Realiza búsqueda con ElasticSearch '''
        if limit == 0:
            limit = None
        if order is None and isinstance(sort, dict):
            # to use a sort function
            ids, total = query_index(cls.__tablename__, queries, offset, limit, sort)
        else:
            ids, total = query_index(cls.__tablename__, queries, offset, limit, sort, order)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i, _id in enumerate(ids):
            when.append((_id, i))
        if not ids:
            return cls.query.filter_by(id=0), total
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        ''' Función antes de enviar commit de db '''
        # pylint: disable=protected-access
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }
        callable_method = 'load_searchable_data'
        for obj in session._changes['add']:
            callable_obj = hasattr(obj, callable_method) and callable(getattr(obj, callable_method))
            if callable_obj and hasattr(obj, '__mapping__'):
                obj.load_searchable_data()
        for obj in session._changes['update']:
            callable_obj = hasattr(obj, callable_method) and callable(getattr(obj, callable_method))
            if callable_obj and hasattr(obj, '__mapping__'):
                obj.load_searchable_data()
        for obj in session._changes['delete']:
            callable_obj = hasattr(obj, callable_method) and callable(getattr(obj, callable_method))
            if callable_obj and hasattr(obj, '__mapping__'):
                obj.load_searchable_data()

    @classmethod
    def after_commit(cls, session):
        ''' Función después de enviar commit de db '''
        # pylint: disable=protected-access
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)

    @classmethod
    def reindex(cls):
        ''' Función para reindexar documentos '''
        clear_doc_type(cls.__tablename__)
        for obj in cls.query:
            obj.load_searchable_data()
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)
