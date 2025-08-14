"""Utilidades de seguridad para el manejo de contraseñas."""

from passlib.hash import bcrypt

def hash_password(password: str) -> str:
    """Genera el hash de una contraseña utilizando bcrypt.

    Args:
        password (str): La contraseña en texto plano.

    Returns:
        str: El hash de la contraseña.
    """
    return bcrypt.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """Verifica si una contraseña en texto plano coincide con su hash.

    Args:
        password (str): La contraseña en texto plano.
        hashed (str): El hash de la contraseña a comparar.

    Returns:
        bool: True si la contraseña coincide, False en caso contrario.
    """
    return bcrypt.verify(password, hashed)
