"""Maneja la lógica relacionada con los modelos"""

from sqlalchemy.sql.functions import ReturnTypeFromArgs
from functions.utils.util import get_model
from functions.general.general import accent

class unaccent(ReturnTypeFromArgs): # pylint: disable=invalid-name
    # pylint: disable=unnecessary-pass
    '''Ignorar tildes'''
    pass


class ManagerGeneral:
    """Clase lógica para manejar modelos"""

    def __init__(self, model):
        self.data = None
        self.allow_deleted = False
        self.model = get_model(model)

    def check_unique_by_field(self, field, value, id_):
        """Retorna true si existe un registro con el campo dado"""
        if id_ is False:
            return self.model.query.filter(
                self.model.deleted == self.allow_deleted,
                unaccent(getattr(self.model, field)) == accent(value)
            ).count() > 0
        return self.model.query.filter(
            self.model.id != id_,
            self.model.deleted == self.allow_deleted
        ).filter(unaccent(getattr(self.model, field)).ilike(accent(value))).count() > 0

    def check_exist(self, filters):
        """Retorna true si existe un registro con la data"""
        query = self.model.query.filter_by(**filters)
        if self.allow_deleted is not None:
            query.filter_by(deleted=self.allow_deleted)
        return query.count() > 0

    def check_exist_in_array(self, values):
        """Retorna true si existe un registro con la data en array"""
        for index, value in enumerate(values):
            filters = {'id': value}
            if not self.check_exist(filters):
                return index, False
        return True
