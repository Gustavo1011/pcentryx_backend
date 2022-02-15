''' Módulo para activar o desactivar un agente '''
import json
import base64
import binascii
from datetime import datetime
from Crypto import Random
from flask import current_app
from Crypto.Cipher import AES
from flask_jwt_extended import create_access_token
from libraries.response import entity_response
from models.user import User

class LoginCRM:  # pylint: disable=too-few-public-methods
    ''' Clase lógica para activar o desactivar un agente '''

    def __call__(self, data):  # pylint: disable=too-many-locals, too-many-branches
        jwt_time_token_old = int(current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
        try:
            data_decrypt = self.decrypt(
                data.get('token'),
                '0b3f0a3bbef12f3a1713e2b4540557002e0d6b6ef06a501154f60070d2c821a3'
            )
        except Exception:
            return entity_response(400, message="Invalid token")

        if 'username' not in data_decrypt or 'password' not in data_decrypt \
            or 'end_date' not in data_decrypt: # noqa: E125
            return entity_response(400, message="Invalid token information structure")

        user = User.query.filter_by(
            username=data_decrypt.get('username'),
            password=data_decrypt.get('password'),
            deleted=False
        ).first()

        due_date = datetime.strptime(
            data_decrypt.get('end_date'), "%Y-%m-%dT%H:%M:%S.%f%z"
        )
        now_local = datetime.now(due_date.tzinfo)
        duration = round((due_date - now_local).total_seconds())
        if duration < 0:
            return entity_response(400, message="The token you enter is already expired")
        if user is None:
            return entity_response(400, message="The user sent has not been found")
        current_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = duration
        try:
            access_token = create_access_token(identity={
                'data': {
                    'id': user.id,
                    'username': user.username
                },
                'related_token_value': data.get('token'),
                'related_token_origin': 'token_crm',
                'timezone': None,
                'end_token': data_decrypt.get('end_date')
            })
        except ValueError:
            current_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = jwt_time_token_old
            return entity_response(400, message="Internal error. Please contact the administrator.")
        current_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = jwt_time_token_old
        return {'token_erp': access_token, 'end_date': data_decrypt.get('end_date')}

    def decrypt(self, data, passphrase):
        def unpad(s):
            return s[:-s[-1]]
        # Poner a bytes la clave
        key = binascii.unhexlify(passphrase)
        # Desencriptación b64 y transformarlo a diccionario
        encrypted = json.loads(base64.b64decode(data).decode('ascii'))
        #Almacenar data y iv
        encrypted_data_1 = encrypted['data']['data']
        encrypted_iv = encrypted['data']['iv']
        # Desencriptar data en bytes
        decrypted_data_in_bytes = base64.b64decode(encrypted_data_1)
        # Desencriptar iv en bytes
        decrypted_iv_in_bytes = base64.b64decode(encrypted_iv)
        # Desencriptar data en bytes
        cipher = AES.new(key, AES.MODE_CBC, decrypted_iv_in_bytes)
        decrypted_data = cipher.decrypt(decrypted_data_in_bytes)
        decrypted_data_unpad = unpad(decrypted_data)
        #Desencriptar ascii
        result = decrypted_data_unpad.decode('ascii').rstrip()
        return json.loads(result.replace("'", '"'))
