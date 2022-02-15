''' Módulo para las operaciones en base de datos '''
import click
from libraries.utils import get_model

def add_model_base(model_base, flask_app, db):
    """ Comandos para los modelos base """

    @model_base.cli.command('cascade_delete')
    @click.argument('entity')
    def cascade_delete(entity): # pylint: disable=unused-variable
        """Cascade delete"""
        value_entity = entity.split(',')
        model_child = get_model(value_entity[0], snake=False)
        result = model_child.query.filter(
            getattr(model_child, value_entity[1]) == value_entity[2]
        ) \
        .all()
        for item in result:
            item.deleted = True
            item.cascade_searchable = True
            db.session.commit()

    @model_base.cli.command('null_entity')
    @click.argument('entity')
    def null_entity(entity): # pylint: disable=unused-variable
        """Set Null Entity"""
        value_entity = entity.split(',')
        model_child = get_model(value_entity[0], snake=False)
        result = model_child.query.filter(
            getattr(model_child, value_entity[1]) == value_entity[2]
        ) \
        .all()
        for item in result:
            setattr(item, value_entity[1], None)
            item.cascade_searchable = True
            db.session.commit()

    flask_app.register_blueprint(model_base)
