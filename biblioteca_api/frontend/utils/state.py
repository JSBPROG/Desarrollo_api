
"""Utilidades para la gestión del estado de la sesión de Streamlit."""

import streamlit as st

def init_session_state():
    """Inicializa las variables de estado de la sesión."""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "token" not in st.session_state:
        st.session_state.token = ""
    if "username" not in st.session_state:
        st.session_state.username = ""
