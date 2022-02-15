''' Módulo para configurar la inyección de dependencias '''
from injector import Binder # pylint: disable=import-self
from flask_injector import FlaskInjector

# Import interfaces
# pylint: disable=line-too-long
from interfaces.users.manage_users import IManageUsers # pylint: disable=no-name-in-module,import-error
from interfaces.users.user_access import IUserAccess # pylint: disable=no-name-in-module,import-error

# Import providers
from providers.manage_users import ManageUsersProvider # pylint: disable=no-name-in-module,import-error
from providers.user_access import UserAccessProvider # pylint: disable=no-name-in-module,import-error

def create_injector(app):
    ''' Conecta la inyección de dependencias con la aplicación '''
    FlaskInjector(app=app, modules=[configure])

def configure(binder: Binder) -> Binder:
    ''' Configura la inyección de dependencias '''
    binder.bind(IManageUsers, ManageUsersProvider())
    binder.bind(IUserAccess, UserAccessProvider())
    return binder
