
"""Vista de autenticación para el inicio de sesión y registro de usuarios."""

import streamlit as st
from services import auth_service

def show_auth_view():
    """Muestra los formularios de inicio de sesión y registro."""
    st.title("Bienvenido a la Biblioteca Digital 📚")
    st.write("Por favor, inicia sesión o regístrate para continuar.")

    login_tab, register_tab = st.tabs(["Iniciar Sesión", "Registrarse"])

    with login_tab:
        with st.form("login_form"):
            username = st.text_input("Nombre de Usuario", key="login_user")
            password = st.text_input("Contraseña", type="password", key="login_pass")
            submitted = st.form_submit_button("Iniciar Sesión")

            if submitted:
                if auth_service.login(username, password):
                    st.rerun()

    with register_tab:
        with st.form("register_form"):
            name = st.text_input("Nombre", key="reg_name")
            lastName = st.text_input("Apellido", key="reg_lastname")
            password = st.text_input("Contraseña", type="password", key="reg_pass")
            submitted = st.form_submit_button("Registrarse")

            if submitted:
                auth_service.register(name, lastName, password)
