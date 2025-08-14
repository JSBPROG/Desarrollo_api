
"""Lógica de negocio para la autenticación de usuarios."""

import streamlit as st
from api import api_client

def login(username: str, password: str) -> bool:
    """Maneja la lógica de inicio de sesión.

    Args:
        username (str): El nombre de usuario.
        password (str): La contraseña.

    Returns:
        bool: True si el inicio de sesión es exitoso, False en caso contrario.
    """
    if not username or not password:
        st.error("Por favor, ingresa tu nombre de usuario y contraseña.")
        return False

    response = api_client.login_user(username, password)
    if response.status_code == 200:
        token = response.json().get("token")
        st.session_state.logged_in = True
        st.session_state.token = token
        st.session_state.username = username
        st.success("¡Inicio de sesión exitoso!")
        return True
    else:
        st.error("Credenciales inválidas. Por favor, inténtalo de nuevo.")
        return False

def register(name: str, lastName: str, password: str):
    """Maneja la lógica de registro de usuarios."""
    if not name or not lastName or not password:
        st.error("Por favor, completa todos los campos.")
        return

    response = api_client.register_user(name, lastName, password)
    if response.status_code == 201:
        st.success("¡Registro exitoso! Ahora puedes iniciar sesión.")
    elif response.status_code == 409:
        st.error("El usuario ya existe. Por favor, elige otro nombre.")
    else:
        st.error("Ocurrió un error durante el registro.")

def logout():
    """Cierra la sesión del usuario."""
    st.session_state.logged_in = False
    st.session_state.token = ""
    st.session_state.username = ""
    st.rerun()
