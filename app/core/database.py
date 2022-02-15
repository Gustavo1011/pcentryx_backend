''' Módulo para la configuración de base de datos '''
from flask_migrate import Migrate, MigrateCommand
from flask_seeder import FlaskSeeder

def add_migration(app, db): # pylint: disable=invalid-name
    ''' Añade las migraciones para la aplicación '''
    Migrate(app, db)
    app.cli.add_command('db', MigrateCommand)

def add_seeders(app, db): # pylint: disable=invalid-name
    ''' Añade los seeders para la aplicación '''
    seeder = FlaskSeeder()
    seeder.init_app(app, db)
