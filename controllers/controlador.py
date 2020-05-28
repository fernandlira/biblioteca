from models.modelos import (Author, Editorial, Libro, User)

class ControladorAutor:

    @classmethod
    def registrar_autor(cls, nombre):
        cls.autor = Author(nombre)
        cls.autor.insert_author()
        print(f"Se registro al autor {nombre} exitosamente")

    @classmethod
    def listar_autores(cls):
        return Author.listar()

class ControladorEditorial:

    @classmethod
    def registrar_editorial(cls, nombre):
        cls.editorial = Editorial(nombre)
        cls.editorial.insert_editorial()

    @classmethod
    def listar_editoriales(cls):
        return Editorial.listar()

class ControladorLibro:

    @classmethod
    def verificar_id(cls,identificador):
        return Libro.verify_id(identificador)

    @classmethod
    def registrar_libro(cls, identificador, nombre, autor, editorial):
        cls.libro = Libro(identificador, nombre, autor, editorial)
        cls.libro.insert_book()
        print(f'Se registro correctamente el libro {nombre}')

    @classmethod
    def verificar_editorial(cls,editorial):
        return Editorial.obtener_ids(editorial)

    @classmethod
    def verificar_autor(cls,autor):
        return Author.verify_id(autor)

    @classmethod
    def listar_libros(cls):
        return Libro.listar()

class ControladorLector:

    @classmethod
    def verificar_id(cls, identificador):
        return User.verify_id(identificador)

    @classmethod
    def registrar_lector(cls, identificador,nombre):
        Usuario = User(identificador,nombre)
        Usuario.insert_user()
        print(f"Se registro al usuario {nombre} exitosamente")

    @classmethod
    def listar_lectores(cls):
        return User.listar()

class ControladorAlquiler:

    @classmethod
    def borrow(cls, book_id, author_id, fecha):
        return Libro.borrow_book(book_id, author_id, fecha)

    @classmethod
    def get_identifiers_list(cls):
        return Libro.get_identifiers_list()


    @classmethod
    def get_identifiers_list2(cls):
        return Libro.get_identifiers_list2()