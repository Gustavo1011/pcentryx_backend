''' Librería para administrar key con Fernet '''

import os
from flask import current_app
from cryptography.fernet import Fernet
from libraries.s3_aws import AdminS3AWS

def read_key():
    ''' Leer la clave en el archivo key.bin, si no lo tiene, se genera '''
    current_app.logger.info("Empezando lectura de archivo key.bin en local")
    admin_s3 = AdminS3AWS()
    if os.path.isfile('key.bin'):
        current_app.logger.info("El archivo key.bin se encontró en local")
        file = open('key.bin', 'rb')
        key = file.read()
        file.close()
    elif admin_s3.check_file('key.bin'):
        current_app.logger.info("El archivo key.bin se encontró en Amazon S3 Bucket")
        object_s3 = admin_s3.get_object('key.bin')
        current_app.logger.info("Descargando archivo key.bin del Amazon S3 Bucket")
        object_s3.download_file('key.bin')
        current_app.logger.info("Leyendo archivo descargado")
        file = open('key.bin', 'rb')
        key = file.read()
        file.close()
    else:
        current_app.logger.info("El archivo key.bin no se encontró en local ni en Amazon S3 Bucket")
        current_app.logger.info("Creando nueva key")
        key = Fernet.generate_key()
        file = open('key.bin', 'wb')
        current_app.logger.info("Escribiendo el archivo key.bin en local")
        file.write(key)
        file.close()
        current_app.logger.info("El archivo key.bin se guardó exitosamente en local: " + \
            ("Sí" if os.path.isfile('key.bin') else "No"))
        current_app.logger.info("Subiendo archivo key.bin en Amazon S3 Bucket")
        admin_s3.upload_file('/key.bin', 'key.bin')
        current_app.logger.info("El archivo key.bin se subió exitosamente en Amazon S3 Bucket: " + \
            ("Sí" if admin_s3.check_file('key.bin') else "No"))
    return key

def generate_password(password):
    ''' Generar clave segura '''
    key = read_key()
    fernet_key = Fernet(key)
    token = fernet_key.encrypt(password.encode())
    decode = token.decode()
    return decode

def compare_password(hash_password, password):
    ''' Comparar clave segura '''
    key = read_key()
    fernet_key = Fernet(key)
    try:
        decrypt = fernet_key.decrypt(hash_password.encode())
    except: # pylint: disable=bare-except
        return False
    return decrypt == password.encode()
