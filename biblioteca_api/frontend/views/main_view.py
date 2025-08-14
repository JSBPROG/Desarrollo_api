
"""Vista principal de la aplicación para la gestión de libros."""

import streamlit as st
import pandas as pd
from datetime import date
from services import book_service
from components import sidebar

def show_main_view():
    """Muestra la interfaz principal de la aplicación."""
    
    sidebar.show_sidebar()

    st.title("📚 Catálogo de Libros")

    books = book_service.get_books()
    if books:
        df = pd.DataFrame(books)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No hay libros en el catálogo todavía. ¡Añade uno!")

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("✍️ Añadir un Nuevo Libro", expanded=False):
            with st.form("new_book_form", clear_on_submit=True):
                title = st.text_input("Título")
                author = st.text_input("Autor")
                language = st.text_input("Idioma")
                published_date_str = st.date_input("Fecha de Publicación", value=None, format="YYYY-MM-DD")
                isbn = st.text_input("ISBN (13 caracteres)")
                pages = st.number_input("Páginas", min_value=1, step=1, value=None)
                
                submitted = st.form_submit_button("Añadir Libro")
                if submitted:
                    book_service.create_book(title, author, language, published_date_str, isbn, pages)

    with col2:
        with st.expander("🔄 Actualizar o Eliminar un Libro", expanded=False):
            if books:
                book_titles = {book['title']: book['id'] for book in books}
                selected_title = st.selectbox("Selecciona un libro para gestionar", options=book_titles.keys())
                
                if selected_title:
                    book_id = book_titles[selected_title]
                    selected_book = next((book for book in books if book['id'] == book_id), None)

                    with st.form("update_book_form"):
                        st.write(f"**Gestionando:** {selected_book['title']}")
                        
                        new_title = st.text_input("Nuevo Título", value=selected_book['title'])
                        new_author = st.text_input("Nuevo Autor", value=selected_book['author'])
                        new_language = st.text_input("Nuevo Idioma", value=selected_book['language'])
                        
                        current_pub_date = None
                        if selected_book.get('published_date'):
                            current_pub_date = date.fromisoformat(selected_book['published_date'])
                        new_published_date = st.date_input("Nueva Fecha de Publicación", value=current_pub_date, format="YYYY-MM-DD")
                        
                        new_isbn = st.text_input("Nuevo ISBN", value=selected_book.get('isbn', ''))
                        new_pages = st.number_input("Nuevas Páginas", min_value=1, step=1, value=selected_book.get('pages'))

                        update_button = st.form_submit_button("Actualizar Libro")
                        
                        if update_button:
                            update_data = {
                                "title": new_title,
                                "author": new_author,
                                "language": new_language,
                                "published_date": str(new_published_date) if new_published_date else None,
                                "isbn": new_isbn,
                                "pages": new_pages
                            }
                            book_service.update_book(book_id, update_data)

                    st.write("---")
                    st.error("Zona de Peligro")
                    if st.button("Eliminar Libro", key=f"delete_{book_id}"):
                        book_service.delete_book(book_id)
            else:
                st.info("Añade un libro primero para poder gestionarlo.")
