"""
main.py: Main project file
"""
import os
from app import app

if __name__ == '__main__':
    APP_HOST = os.getenv('APP_HOST', "127.0.0.1")
    APP_PORT = os.getenv('APP_PORT', "5000")
    DEBUG = os.getenv('DEBUG', "True")
    app.run(host=APP_HOST, port=APP_PORT, debug=(DEBUG == "True"))
