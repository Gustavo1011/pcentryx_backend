''' Módulo para la configuración de SMTP '''
from flask_mail import Mail

def create_mail_app(app):
    ''' Incorpora soporte de Mail a la aplicación '''
    mail = Mail()
    mail.init_app(app)
    return mail
