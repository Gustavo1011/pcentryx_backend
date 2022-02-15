"""
manage_fields_db.py: File to define ManageFieldsDB
"""
from app import db
from functions.utils.util import snake_case, get_plural

class ManageRelationsDB():
    """DB fields Manager"""
    def __init__(self, model_name):
        self.model_name = model_name
        self.snake_name = snake_case(model_name)
        self.plural_name = get_plural(self.snake_name)

    def has_one(self, model_name_to_relate):
        return db.relationship(
            model_name_to_relate,
            back_populates=self.plural_name,
        )

    def has_many(self, model_name_to_relate):
        return db.relationship(
            model_name_to_relate,
            back_populates=self.snake_name,
            lazy='dynamic'
        )

