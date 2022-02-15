from functions.utils.util import get_model, get_fields_mapping

class Searcher():
    def __init__(self, model_base, data=None):
        self.model_base = model_base
        self.data = data
        if self.data.get('sort') is None:
            self.data['sort'] = 'id'
        if self.data.get('order') is None:
            self.data['order'] = 'asc'
        if self.data.get('page') is None:
            self.data['page'] = 1
        self.related_models = [{'name': model_base, 'model': get_model(model_base)}]
        self.query = self.related_models[0]['model'].query
        self.vars = {}
        self.filters = []
        for clave, valor in get_fields_mapping(model_base).items():
            self.vars[clave] = getattr(self.related_models[0]['model'], clave)

    def set_filters(self, filters):
        filters_array = []
        for filter_ in filters:
            translation = filter_.translate(self.vars)
            if len(translation) > 0:
                filters_array.append(*translation)
        self.query = self.query.filter(*filters_array)

    def get_results(self):
        if self.has_ordering():
            self.query = self.query.order_by(
                getattr(self.vars[self.data.get('sort')], self.data['order'])()
            )
        if self.has_pagination():
            return self.query.paginate(
                page=self.data['page'],
                per_page=self.data['limit'],
                error_out=False
            ).items
        return self.query.all()

    def get_total(self):
        return self.query.count()

    def has_pagination(self):
        return (
            self.data is not None and
            self.data.get('limit') is not None and
            self.data.get('page') is not None
        )

    def has_ordering(self):
        return (
            self.data is not None and
            self.data.get('sort') is not None and
            self.data.get('order') is not None
        )