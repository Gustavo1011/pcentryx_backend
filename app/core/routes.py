''' Módulo para crear los comandos de la aplicación '''
from flask import send_file

def create_routes(app, db): # pylint: disable=invalid-name
    ''' Añade comandos a la aplicación '''
    @app.route('/response_test', methods=['GET'])
    def response_test(): # pylint: disable=unused-variable
        return "Test"

    @app.route('/debug-sentry')
    def trigger_error(): # pylint: disable=unused-variable
        division_by_zero = 1 / 0
        print(division_by_zero)

    return app
