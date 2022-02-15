'''status_messages.py: Define messages acording the status'''

class StatusMessages:
    '''Class to define messages acording the status'''

    def __init__(self):
        self.status_messages = {
            200: 'Registration has been successful',
            201: 'Registration has been successful',
            400: 'Bad Request',
            404: 'Object not found',
            500: 'Internal Server Error'
        }
