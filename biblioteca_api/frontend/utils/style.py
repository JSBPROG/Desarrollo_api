
"""Utilidades para la estilización de la aplicación con CSS."""

import streamlit as st

def load_css():
    """Carga el CSS personalizado para la aplicación."""
    st.markdown("""
        <style>
            .stApp {
                background-color: #f0f2f6;
            }
            .stButton>button {
                width: 100%;
                border-radius: 10px;
            }
            .stTextInput>div>div>input, .stDateInput>div>div>input, .stNumberInput>div>div>input {
                border-radius: 10px;
            }
            .st-emotion-cache-1y4p8pa {
                padding-top: 2rem;
            }
        </style>
    """, unsafe_allow_html=True)
