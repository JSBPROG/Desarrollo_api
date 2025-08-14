"""Rutas de la API para la gestión de libros."""

from flask import Blueprint, jsonify, request
from backend.controllers import books_controller
from backend.utils.jwt_handler import token_required
from backend.utils.validators import BookSchema, validate_json

bp = Blueprint('books', __name__, url_prefix='/books')

@bp.route('/', methods=['GET'])
def get_books():
    """Obtiene una lista de todos los libros."""
    books = books_controller.get_all_books_controller()
    return jsonify([book.to_dict() for book in books])

@bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id: int):
    """Obtiene un libro por su ID."""
    book = books_controller.get_book_by_id_controller(book_id)
    if not book:
        return jsonify({'message': 'Libro no encontrado'}), 404
    return jsonify(book.to_dict())

@bp.route('/', methods=['POST'])
@token_required
def create_book(current_user):
    """Crea un nuevo libro."""
    data = request.get_json()
    errors = validate_json(BookSchema(), data)
    if errors:
        return jsonify(errors), 400
    
    book = books_controller.create_book_controller(data)
    return jsonify(book.to_dict()), 201

@bp.route('/<int:book_id>', methods=['PUT'])
@token_required
def update_book(current_user, book_id: int):
    """Actualiza un libro existente."""
    data = request.get_json()
    errors = validate_json(BookSchema(), data)
    if errors:
        return jsonify(errors), 400

    book = books_controller.update_book_controller(book_id, data)
    
    if not book:
        return jsonify({'message': 'Libro no encontrado'}), 404
        
    return jsonify(book.to_dict())

@bp.route('/<int:book_id>', methods=['DELETE'])
@token_required
def delete_book(current_user, book_id: int):
    """Elimina un libro."""
    success = books_controller.delete_book_controller(book_id)
    if not success:
        return jsonify({'message': 'Libro no encontrado'}), 404
        
    return jsonify({'message': 'Libro eliminado correctamente'})
