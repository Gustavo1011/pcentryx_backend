''' Módulo para activar o desactivar un agente '''
import json
from datetime import datetime
from base64 import b64decode
from flask import current_app
from Crypto.Cipher import AES
from flask_jwt_extended import create_access_token
from libraries.response import entity_response
from models.user import User

class LoginCore:  # pylint: disable=too-few-public-methods
    ''' Clase lógica para activar o desactivar un agente '''

    def __call__(self, data):  # pylint: disable=too-many-locals, too-many-branches
        jwt_time_token_old = int(current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
        try:
            data_decrypt = json.loads(self.decrypt(
                't20cli99k0g1ef07C0r3_379R#dG34h1'.encode(),
                data.get('token')
            ))
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
                'related_token_origin': 'token_core',
                'timezone': None,
                'end_token': data_decrypt.get('end_date')
            })
        except ValueError:
            current_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = jwt_time_token_old
            return entity_response(400, message="Internal error. Please contact the administrator.")
        current_app.config['JWT_ACCESS_TOKEN_EXPIRES'] = jwt_time_token_old
        return {'token_erp': access_token, 'end_date': data_decrypt.get('end_date')}

    def decrypt(self, key, str_byte):
        """Funcion para desencriptar"""
        data = b64decode(str_byte.encode())
        nonce = data[0:8] + data[16:24]
        tag = data[8:16] + data[24:32]
        ciphertext = data[AES.block_size * 2:]
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        return cipher.decrypt_and_verify(ciphertext, tag)
