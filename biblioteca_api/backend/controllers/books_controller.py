"""Controladores para la gestión de libros."""

from backend.services import books_service
from backend.models.book import Book

def get_all_books_controller() -> list[Book]:
    """Controlador para obtener todos los libros."""
    return books_service.get_all_books()

def get_book_by_id_controller(book_id: int) -> Book | None:
    """Controlador para obtener un libro por su ID."""
    return books_service.get_book_by_id(book_id)

def create_book_controller(data: dict) -> Book:
    """Controlador para crear un nuevo libro."""
    return books_service.create_book(data)

def update_book_controller(book_id: int, data: dict) -> Book | None:
    """Controlador para actualizar un libro existente."""
    return books_service.update_book(book_id, data)

def delete_book_controller(book_id: int) -> bool:
    """Controlador para eliminar un libro."""
    return books_service.delete_book(book_id)
