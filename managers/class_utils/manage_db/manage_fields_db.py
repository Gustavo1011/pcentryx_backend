"""
manage_fields_db.py: File to define ManageFieldsDB
"""
from app import db
from functions.utils.util import snake_case, get_plural

class ManageFieldsDB():
    """DB fields Manager"""
    @staticmethod
    def db_primary_key():
        return db.Column(
            db.Integer,
            primary_key=True,
            autoincrement=True,
            index=True
        )

    @staticmethod
    def db_integer(nullable=False, default=0):
        return db.Column(
            db.Integer,
            nullable=nullable,
            default=default
        )

    @staticmethod
    def db_string(size, nullable=False):
        return db.Column(
            db.String(size), nullable=nullable
        )

    @staticmethod
    def db_text(nullable=False):
        return db.Column(db.Text(), nullable=nullable)

    @staticmethod
    def db_foreign_key(model_name, nullable=False):
        table_name = get_plural(snake_case(model_name))
        return db.Column(
            db.Integer, db.ForeignKey(
                '{}.id'.format(table_name), ondelete='CASCADE'
            ),
            nullable=nullable, comment='{} ID'.format(table_name)
        )

    @staticmethod
    def db_datetime(nullable=False, default=False):
        if default:
            return db.Column(
                db.DateTime(timezone=True), nullable=nullable,
                default=default
            )
        return db.Column(
            db.DateTime(timezone=True), nullable=nullable
        )

    @staticmethod
    def db_date(nullable=False, default=False):
        if default:
            return db.Column(
                db.Date, nullable=nullable,
                default=default
            )
        return db.Column(
            db.Date, nullable=nullable
        )

    @staticmethod
    def db_boolean(nullable=False, default=False):
        return db.Column(
            db.Boolean, nullable=nullable, default=default
        )

    @staticmethod
    def db_decimal(size, decimal_size, nullable=False, default=None):
        return db.Column(
            db.DECIMAL(size, decimal_size), nullable=nullable, default=default
        )

