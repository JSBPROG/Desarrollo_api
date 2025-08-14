"""Lógica de negocio para la gestión de libros."""

from backend.models import db
from backend.models.book import Book

def get_all_books() -> list[Book]:
    """Obtiene todos los libros de la base de datos.

    Returns:
        list[Book]: Una lista de todos los libros.
    """
    return Book.query.all()

def get_book_by_id(book_id: int) -> Book | None:
    """Obtiene un libro por su ID.

    Args:
        book_id (int): El ID del libro a buscar.

    Returns:
        Book | None: El libro si se encuentra, o None.
    """
    return Book.query.get(book_id)

def create_book(data: dict) -> Book:
    """Crea un nuevo libro en la base de datos.

    Args:
        data (dict): Un diccionario con los datos del libro.

    Returns:
        Book: La instancia del libro creado.
    """
    new_book = Book(
        title=data.get('title'),
        author=data.get('author'),
        published_date=data.get('published_date'),
        isbn=data.get('isbn'),
        pages=data.get('pages'),
        language=data.get('language')
    )
    db.session.add(new_book)
    db.session.commit()
    return new_book

def update_book(book_id: int, data: dict) -> Book | None:
    """Actualiza un libro existente.

    Args:
        book_id (int): El ID del libro a actualizar.
        data (dict): Un diccionario con los nuevos datos del libro.

    Returns:
        Book | None: El libro actualizado si se encuentra, o None.
    """
    book = get_book_by_id(book_id)
    if not book:
        return None

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.published_date = data.get('published_date', book.published_date)
    book.isbn = data.get('isbn', book.isbn)
    book.pages = data.get('pages', book.pages)
    book.language = data.get('language', book.language)

    db.session.commit()
    return book

def delete_book(book_id: int) -> bool:
    """Elimina un libro de la base de datos.

    Args:
        book_id (int): El ID del libro a eliminar.

    Returns:
        bool: True si el libro fue eliminado, False en caso contrario.
    """
    book = get_book_by_id(book_id)
    if not book:
        return False

    db.session.delete(book)
    db.session.commit()
    return True
