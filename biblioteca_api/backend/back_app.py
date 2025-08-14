"""Punto de entrada de la aplicación Flask."""

from flask import Flask, jsonify
from backend.models import db
from backend.config import Config
from backend.routes import auth_routes, books_routes

def create_app(config_class=Config) -> Flask:
    """Crea y configura una instancia de la aplicación Flask.

    Args:
        config_class: La clase de configuración a utilizar.

    Returns:
        Flask: La instancia de la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(books_routes.bp)

    with app.app_context():
        db.create_all()

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"message": "Recurso no encontrado"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"message": "Error interno del servidor"}), 500

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
