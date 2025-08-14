"""Validadores de esquemas para los datos de entrada de la API."""

from marshmallow import Schema, fields, validate, ValidationError

class UserRegisterSchema(Schema):
    """Esquema para la validación de los datos de registro de usuario."""
    name = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    lastName = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    password = fields.Str(required=True, validate=validate.Length(min=6))

class UserLoginSchema(Schema):
    """Esquema para la validación de los datos de inicio de sesión."""
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class BookSchema(Schema):
    """Esquema para la validación de los datos de los libros."""
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    author = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    published_date = fields.Date(required=False, allow_none=True)
    isbn = fields.Str(required=False, allow_none=True, validate=validate.Length(equal=13))
    pages = fields.Int(required=False, allow_none=True, validate=validate.Range(min=1))
    language = fields.Str(required=True, validate=validate.Length(min=2, max=50))

def validate_json(schema: Schema, data: dict) -> dict | None:
    """Valida un diccionario de datos contra un esquema de Marshmallow.

    Args:
        schema (Schema): La instancia del esquema con la que validar.
        data (dict): El diccionario con los datos a validar.

    Returns:
        dict | None: Un diccionario con los errores de validación o None si es válido.
    """
    try:
        schema.load(data)
        return None
    except ValidationError as err:
        return err.messages
