"""Módulo de inicialización de la base de datos.

Este módulo crea una instancia de SQLAlchemy que será utilizada por los modelos
y la aplicación Flask.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

