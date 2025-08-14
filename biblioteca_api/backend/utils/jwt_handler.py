"""Utilidades para el manejo de JSON Web Tokens (JWT)."""

import jwt as pyjwt
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import request, jsonify
from backend.config import Config
from backend.models.user import User

CRYPTOGRAPHY = 'HS256'

def encode_token(user_id: int) -> str:
    """Genera un token JWT para un ID de usuario dado.

    Args:
        user_id (int): El ID del usuario para el que se genera el token.

    Returns:
        str: El token JWT codificado.
    """
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1),
        'iat': datetime.now(timezone.utc),
        'sub': user_id
    }
    return pyjwt.encode(
        payload,
        Config.JWT_SECRET_KEY,
        algorithm=CRYPTOGRAPHY
    )

def decode_token(token: str) -> int | str:
    """Decodifica un token JWT y extrae el ID del usuario.

    Args:
        token (str): El token JWT a decodificar.

    Returns:
        int | str: El ID del usuario si el token es válido, o un mensaje de error.
    """
    try:
        payload = pyjwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[CRYPTOGRAPHY])
        return payload['sub']
    except pyjwt.ExpiredSignatureError:
        return 'El token ha expirado. Por favor, inicie sesión de nuevo.'
    except pyjwt.InvalidTokenError:
        return 'Token inválido. Por favor, inicie sesión de nuevo.'

def token_required(f):
    """Decorador para proteger rutas que requieren autenticación mediante JWT.

    Args:
        f (function): La función de la vista a decorar.

    Returns:
        function: La función decorada.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'message': 'Falta el token de autenticación'}), 401

        try:
            user_id = decode_token(token)
            if isinstance(user_id, str):
                return jsonify({'message': user_id}), 401

            current_user = User.query.get(user_id)
            if not current_user:
                return jsonify({'message': 'Usuario no encontrado'}), 401

        except Exception:
            return jsonify({'message': 'El token es inválido'}), 401

        return f(current_user, *args, **kwargs)
    return decorated
