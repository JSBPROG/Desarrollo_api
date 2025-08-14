"""Controladores para la autenticación de usuarios."""

from backend.services import auth_service

def register_user_controller(data: dict) -> dict | None:
    """Controlador para registrar un nuevo usuario."""
    return auth_service.register_user(data)

def login_user_controller(username: str, password: str) -> str | None:
    """Controlador para iniciar sesión de un usuario."""
    return auth_service.authenticate(username, password)
