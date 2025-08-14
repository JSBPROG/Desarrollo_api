"""Configuración de la aplicación Flask."""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuración de la aplicación Flask.

    Las variables se cargan desde el entorno, lo que permite flexibilidad
    para distintos entornos (desarrollo, producción, etc.).
    """
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave-secreta-para-proteger-sesiones")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///biblioteca.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "clave-secreta-para-jwt-muy-segura")

