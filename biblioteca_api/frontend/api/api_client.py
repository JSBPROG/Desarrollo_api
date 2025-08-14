"""Cliente de la API para interactuar con el backend de la biblioteca."""

import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:5000"

def get_auth_headers() -> dict:
    """Obtiene los encabezados de autorización con el token de sesión."""
    if "token" in st.session_state and st.session_state.token:
        return {"x-access-token": st.session_state.token}
    return {}

# --- Endpoints de Autenticación ---

def register_user(name: str, lastName: str, password: str) -> requests.Response:
    """Registra un nuevo usuario en la API."""
    url = f"{BASE_URL}/auth/register"
    payload = {"name": name, "lastName": lastName, "password": password}
    response = requests.post(url, json=payload)
    return response

def login_user(username: str, password: str) -> requests.Response:
    """Inicia sesión de un usuario en la API."""
    url = f"{BASE_URL}/auth/login"
    payload = {"username": username, "password": password}
    response = requests.post(url, json=payload)
    return response

# --- Endpoints de Libros ---

def get_all_books() -> requests.Response:
    """Obtiene todos los libros de la API."""
    url = f"{BASE_URL}/books/"
    response = requests.get(url)
    return response

def get_book_by_id(book_id: int) -> requests.Response:
    """Obtiene un libro por su ID de la API."""
    url = f"{BASE_URL}/books/{book_id}"
    response = requests.get(url)
    return response

def create_book(title: str, author: str, language: str, published_date: str = None, isbn: str = None, pages: int = None) -> requests.Response:
    """Crea un nuevo libro en la API."""
    url = f"{BASE_URL}/books/"
    payload = {
        "title": title,
        "author": author,
        "language": language,
        "published_date": published_date,
        "isbn": isbn,
        "pages": pages,
    }
    payload = {k: v for k, v in payload.items() if v is not None and v != ""}
    headers = get_auth_headers()
    response = requests.post(url, json=payload, headers=headers)
    return response

def update_book(book_id: int, data: dict) -> requests.Response:
    """Actualiza un libro existente en la API."""
    url = f"{BASE_URL}/books/{book_id}"
    payload = {k: v for k, v in data.items() if v is not None and v != ""}
    headers = get_auth_headers()
    response = requests.put(url, json=payload, headers=headers)
    return response

def delete_book(book_id: int) -> requests.Response:
    """Elimina un libro de la API."""
    url = f"{BASE_URL}/books/{book_id}"
    headers = get_auth_headers()
    response = requests.delete(url, headers=headers)
    return response
