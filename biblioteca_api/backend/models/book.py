from __future__ import annotations
from datetime import date, datetime
from typing import Optional

from backend.models import db
from sqlalchemy import String, Integer, Date, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column


class Book(db.Model):
    """Modelo de la base de datos para un libro.

    Atributos:
        id (int): Identificador único del libro.
        title (str): Título del libro.
        author (str): Autor del libro.
        published_date (Optional[date]): Fecha de publicación del libro.
        isbn (Optional[str]): ISBN del libro.
        pages (Optional[int]): Número de páginas del libro.
        language (str): Idioma del libro.
        created_at (datetime): Fecha de creación del registro.
        updated_at (datetime): Fecha de última actualización del registro.
    """

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False, unique=True, index=True)
    author: Mapped[str] = mapped_column(String(120), nullable=False)
    published_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    isbn: Mapped[Optional[str]] = mapped_column(String(13), unique=True, nullable=True, index=True)
    pages: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    language: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        """Representación en cadena del objeto Book."""
        return f"<Book {self.title} by {self.author}>"

    def to_dict(self) -> dict:
        """Convierte el objeto Book a un diccionario.

        Returns:
            dict: Un diccionario con los datos del libro.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "published_date": self.published_date.isoformat() if self.published_date else None,
            "isbn": self.isbn,
            "pages": self.pages,
            "language": self.language,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


