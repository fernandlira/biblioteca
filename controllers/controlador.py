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
        libro = Libro(identificador, nombre, autor, editorial)
        libro.insert_book()
        print(f'Se registro correctamente el libro {nombre}')

    @classmethod
    def verificar_editorial(cls,editorial):
        return Editorial.obtener_ids(editorial)

    @classmethod
    def verificar_autor(cls,autor):
        return Author.verify_id(autor)

    @classmethod
    def verificar_libros_alquilados(cls,identifier):
        return Libro.verify_if_borrowed(identifier)

    @classmethod
    def listar_libros(cls):
        return Libro.listar()

    @classmethod
    def listar_libros_disponibles(cls):
        return Libro.listar_disponibles()

    @classmethod
    def devolver(cls,identifier):
        return Libro.devolver(identifier)

# Funcion ELiminar
    @classmethod
    def eliminar_libro(cls, identificador):
        return Libro.eliminar_libro(identificador)

    @classmethod
    def eliminar_alquiler(cls, libro):
        return Libro.eliminar_libro_alquiler(libro)

class ControladorLector:

    @classmethod
    def verificar_id(cls, identificador):
        return User.verify_id(identificador)

    @classmethod
    def verificar_id_existente(cls, identificador):
        return User.verify_id_exists(identificador)

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
    def verificar_id(cls,identificador):
        return Libro.alquiler_verify_id(identificador)

    @classmethod
    def borrow(cls,ids,u_idenficador):
        for ide in ids:
            Libro.borrow_book(ide,u_idenficador)
            print(f"Alquiler del libro {ide} completado!")

    @classmethod
    def listado(cls):
        return Libro.listar_borrow()