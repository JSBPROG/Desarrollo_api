
"""Punto de entrada principal para la aplicación de frontend de la Biblioteca Digital."""

import streamlit as st
from utils import style, state
from views import auth_view, main_view

st.set_page_config(
    page_title="Biblioteca Digital",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

state.init_session_state()
style.load_css()

def main():
    """Función principal para ejecutar la aplicación."""
    if st.session_state.logged_in:
        main_view.show_main_view()
    else:
        auth_view.show_auth_view()

if __name__ == "__main__":
    main()
