
"""Componente de la barra lateral de la aplicación."""

import streamlit as st
from services import auth_service

def show_sidebar():
    """Muestra la barra lateral de la aplicación."""
    with st.sidebar:
        st.title(f"Hola, {st.session_state.username}!")
        st.write("---")
        if st.button("Cerrar Sesión"):
            auth_service.logout()
        
        st.write("---")
        st.info("Gestiona los libros de la biblioteca desde esta interfaz.")
