from flask_socketio import SocketIO

socketio = SocketIO(
    cors_allowed_origins = []
)

def initalize_socket_app(flask_app):
    ''' Inicializa socketio en la aplicación Flask '''
    socketio.init_app(flask_app)
