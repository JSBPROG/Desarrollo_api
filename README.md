# Biblioteca API

Este proyecto es una aplicación web completa para la gestión de una biblioteca digital. Incluye un backend RESTful API construido con Flask y un frontend interactivo construido con Streamlit.

## Arquitectura

La aplicación está dividida en dos componentes principales: el backend y el frontend.

### Backend

El backend es una API RESTful construida con Flask, siguiendo una arquitectura en capas para una clara separación de responsabilidades:

- **`models`**: Define los modelos de la base de datos (Libro y Usuario) utilizando Flask-SQLAlchemy.
- **`services`**: Contiene la lógica de negocio de la aplicación (ej. cómo crear, actualizar o eliminar un libro).
- **`controllers`**: Maneja las solicitudes HTTP y las respuestas, actuando como un puente entre las rutas y los servicios.
- **`routes`**: Define los endpoints de la API (ej. `/books`, `/auth/login`).
- **`utils`**: Incluye utilidades para tareas como la validación de datos (con Marshmallow), el manejo de JWT y el hash de contraseñas.
- **`config.py`**: Gestiona la configuración de la aplicación, cargando variables de entorno para mayor seguridad y flexibilidad.
- **`back_app.py`**: Es el punto de entrada de la aplicación Flask, donde se crea y configura la aplicación.

### Frontend

El frontend es una aplicación de una sola página (SPA) construida con Streamlit, que consume la API del backend. La estructura del frontend también es modular:

- **`api`**: Contiene el cliente de la API (`api_client.py`) que se encarga de hacer las peticiones al backend.
- **`views`**: Define las diferentes "páginas" o vistas de la aplicación (autenticación y vista principal).
- **`services`**: Contiene la lógica de la interfaz de usuario (ej. qué hacer cuando un usuario hace clic en el botón de login).
- **`components`**: Almacena componentes de UI reutilizables, como la barra lateral.
- **`utils`**: Incluye utilidades para la gestión del estado de la sesión y la estilización de la aplicación.
- **`app.py`**: Es el punto de entrada de la aplicación Streamlit.

## Tecnologías Utilizadas

- **Backend**: Python, Flask, Flask-SQLAlchemy, Marshmallow, python-dotenv, Passlib, PyJWT.
- **Frontend**: Python, Streamlit, requests, pandas.
- **Base de Datos**: SQLite (por defecto).

## Funcionalidades

- Registro y autenticación de usuarios mediante JSON Web Tokens (JWT).
- Gestión completa de libros (Crear, Leer, Actualizar, Eliminar - CRUD).
- Interfaz de usuario web interactiva y fácil de usar.

## Pasos para la Instalación y Ejecución

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2.  **Configurar el entorno virtual (recomendado):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar las variables de entorno:**
    Crea un archivo `.env` en la raíz del proyecto, basándote en el archivo `.env.example`.

5.  **Ejecutar el backend:**
    ```bash
    cd biblioteca_api
    python -m backend.back_app.py
    ```
    El servidor del backend se ejecutará en `http://127.0.0.1:5000`.

6.  **Ejecutar el frontend:**
    En una nueva terminal, navega a la carpeta del frontend y ejecuta la aplicación Streamlit:
    ```bash
    cd biblioteca_api/frontend
    streamlit run app.py
    ```
    La aplicación frontend estará disponible en la URL que se muestre en la terminal (normalmente `http://localhost:8501`).
