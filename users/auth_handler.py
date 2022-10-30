import time
from typing import Dict
import jwt
from jwt import PyJWT
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload=payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

# secret=please_please_update_me_please
# algorithm=HS256
# import os
# import binascii
# binascii.hexlify(os.urandom(24))
# b'deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f'
