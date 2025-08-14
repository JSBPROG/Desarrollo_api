"""Rutas de la API para la autenticación de usuarios."""

from flask import Blueprint, request, jsonify
from backend.controllers import auth_controller
from backend.utils.validators import UserRegisterSchema, UserLoginSchema, validate_json

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    """Registra un nuevo usuario."""
    data = request.get_json()
    errors = validate_json(UserRegisterSchema(), data)
    if errors:
        return jsonify(errors), 400

    user = auth_controller.register_user_controller(data)

    if user is None:
        return jsonify({'message': 'El usuario ya existe'}), 409

    return jsonify(user), 201

@bp.route('/login', methods=['POST'])
def login():
    """Inicia sesión de un usuario."""
    data = request.get_json()
    errors = validate_json(UserLoginSchema(), data)
    if errors:
        return jsonify(errors), 400

    username = data.get('username')
    password = data.get('password')

    token = auth_controller.login_user_controller(username, password)

    if not token:
        return jsonify({'message': 'Credenciales inválidas'}), 401

    return jsonify({'token': token})
