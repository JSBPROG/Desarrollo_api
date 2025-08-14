from __future__ import annotations
from backend.models import db
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from backend.utils.security import hash_password, verify_password


class User(db.Model):
    """Modelo de la base de datos para un usuario.

    Atributos:
        id (int): Identificador único del usuario.
        name (str): Nombre del usuario.
        lastName (str): Apellido del usuario.
        passwd (str): Hash de la contraseña del usuario.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    lastName: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    passwd: Mapped[str] = mapped_column(String(128), nullable=False)

    def __repr__(self) -> str:
        """Representación en cadena del objeto User."""
        return f"<User {self.name} {self.lastName}>"

    def to_dict(self) -> dict:
        """Convierte el objeto User a un diccionario.

        Returns:
            dict: Un diccionario con los datos del usuario.
        """
        return {
            "id": self.id,
            "name": self.name,
            "lastName": self.lastName,
        }

    def set_password(self, password: str):
        """Hashea y establece la contraseña del usuario.

        Args:
            password (str): La contraseña en texto plano.
        """
        self.passwd = hash_password(password)

    def check_password(self, password: str) -> bool:
        """Verifica si la contraseña proporcionada coincide con la almacenada.

        Args:
            password (str): La contraseña en texto plano a verificar.

        Returns:
            bool: True si la contraseña es correcta, False en caso contrario.
        """
        return verify_password(password, self.passwd)
