
"""Lógica de negocio para la gestión de libros."""

import streamlit as st
from api import api_client

def get_books() -> list:
    """Obtiene todos los libros de la API."""
    response = api_client.get_all_books()
    if response.status_code == 200:
        return response.json()
    else:
        st.error("No se pudo cargar el catálogo de libros.")
        return []

def create_book(title: str, author: str, language: str, published_date: str, isbn: str, pages: int):
    """Maneja la lógica de creación de libros."""
    if not all([title, author, language]):
        st.warning("Título, Autor e Idioma son campos obligatorios.")
        return

    pub_date = str(published_date) if published_date else None
    response = api_client.create_book(title, author, language, pub_date, isbn, pages)
    if response.status_code == 201:
        st.success("¡Libro añadido con éxito!")
        st.rerun()
    else:
        st.error(f"Error al añadir el libro: {response.json().get('message', 'Error desconocido')}")

def update_book(book_id: int, data: dict):
    """Maneja la lógica de actualización de libros."""
    response = api_client.update_book(book_id, data)
    if response.status_code == 200:
        st.success("¡Libro actualizado con éxito!")
        st.rerun()
    else:
        st.error(f"Error al actualizar: {response.json().get('message', 'Error desconocido')}")

def delete_book(book_id: int):
    """Maneja la lógica de eliminación de libros."""
    response = api_client.delete_book(book_id)
    if response.status_code == 200:
        st.success("¡Libro eliminado con éxito!")
        st.rerun()
    else:
        st.error(f"Error al eliminar: {response.json().get('message', 'Error desconocido')}")
