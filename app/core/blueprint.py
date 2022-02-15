''' Módulo para la configuración de aplicación base '''
import time
import click
from flask_migrate import migrate, upgrade
from seeds.seed import DatabaseSeed, UnitSeed

import datetime


def add_blueprint(bp, flask_app, db, config):
    @bp.cli.command('cleanall')
    def clean_all():
        flask_app.config['ELASTICSEARCH_REFRESH'] = 'false'
        print(str(datetime.datetime.now()) + " Clear all")
        clear_all(flask_app, db, config)

    @bp.cli.command('postbackup')
    def post_backup():
        refresh_temporary = flask_app.config['ELASTICSEARCH_REFRESH']
        flask_app.config['ELASTICSEARCH_REFRESH'] = 'false'
        print(str(datetime.datetime.now()) + " elasticsearch indexing")
        db.engine.execute("CREATE EXTENSION unaccent;")
        flask_app.config['ELASTICSEARCH_REFRESH'] = refresh_temporary

    @bp.cli.command('recreate')
    def recreate():
        clear_all(flask_app, db, config)
        print(str(datetime.datetime.now()) + " Upgrade migrations")
        upgrade()
        print(str(datetime.datetime.now()) + " Start Seeding")
        database_seed = DatabaseSeed(db)
        database_seed.run()
        db.engine.execute("CREATE EXTENSION unaccent;")

    @bp.cli.command('remigrate')
    def remigrate():
        refresh_temporary = flask_app.config['ELASTICSEARCH_REFRESH']
        flask_app.config['ELASTICSEARCH_REFRESH'] = 'false'
        clear_all(flask_app, db, config)
        migrate()
        upgrade()
        database_seed = DatabaseSeed(db)
        database_seed.run()
        db.engine.execute("CREATE EXTENSION unaccent;")
        flask_app.config['ELASTICSEARCH_REFRESH'] = refresh_temporary

    @bp.cli.command('seed')
    def run_seed():
        """Run the seeds"""
        database_seed = DatabaseSeed(db)
        database_seed.run()

    @bp.cli.command('unit_seed')
    @click.argument("name")
    def run_unit_seed(name):
        """Run the seed"""
        unit_seed = UnitSeed(db, name)
        unit_seed.run()

    @bp.cli.command('part_seed')
    @click.argument("number_part")
    def run_part_seed(number_part):
        """Run the seed"""
        unit_seed = DatabaseSeed(db)
        unit_seed.run_part(int(number_part))

    @bp.cli.command('create_module')
    @click.argument("module_name")
    @click.argument("api_name")
    @click.argument("version")
    def create_module(module_name, api_name, version):
        """Run the seed"""
        from managers.class_utils.writer.writer_module import WriterModule
        writer = WriterModule(module_name, api_name, version)
        writer.writer()

    @bp.cli.command('test')
    def run_test():
        """Run the seeds"""
        print('TEST')
        from factories.brands.brand_builder import BrandBuilder
        data = BrandBuilder().with_name('Victor LLancari').with_deleted(True).build()
        print(data.__dict__)

    @bp.cli.command('generate_swagger')
    @click.argument("module_name")
    @click.argument("api_name")
    @click.argument("version")
    def generate_swagger(module_name, api_name, version):
        """Run the seeds"""
        from managers.class_utils.writer.automate_swagger import AutomateSwagger
        writer = AutomateSwagger(module_name, api_name, version)
        writer.write()

    flask_app.register_blueprint(bp)


def clear_all(flask_app, db, config):
    if config != 'develop':
        time.sleep(10)
    time.sleep(10)
    db.engine.execute("DROP SCHEMA IF EXISTS public CASCADE;")
    db.engine.execute("CREATE SCHEMA IF NOT EXISTS public;")


def preprocessing_string(value):
    from functions.general.general import accent
    from functions.utils.util import remove_extra_spaces

    return accent(remove_extra_spaces(value))
