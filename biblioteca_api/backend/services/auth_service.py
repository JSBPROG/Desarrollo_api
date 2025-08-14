"""Lógica de negocio para la autenticación de usuarios."""

from backend.models import db
from backend.models.user import User
from backend.utils.jwt_handler import encode_token

def register_user(data: dict) -> dict | None:
    """Registra un nuevo usuario en la base de datos.

    Args:
        data (dict): Un diccionario con los datos del usuario.

    Returns:
        dict | None: Un diccionario con los datos del usuario creado o None si ya existe.
    """
    name = data.get('name')
    lastName = data.get('lastName')
    password = data.get('password')

    if User.query.filter_by(name=name).first():
        return None

    new_user = User(name=name, lastName=lastName)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict()

def authenticate(username: str, password: str) -> str | None:
    """Autentica a un usuario y devuelve un token JWT si es válido.

    Args:
        username (str): El nombre de usuario.
        password (str): La contraseña del usuario.

    Returns:
        str | None: El token JWT si la autenticación es exitosa, o None.
    """
    user = User.query.filter_by(name=username).first()

    if user and user.check_password(password):
        return encode_token(user.id)
    
    return None
