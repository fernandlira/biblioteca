from models.modelos import (Author, Editorial, Libro, User)

class ControladorAutor:

    @classmethod
    def create(cls, nombre):
        cls.autor = Author(nombre)
        cls.autor.insert_author()
        print(f"Se registro al autor {nombre} exitosamente")

    @classmethod
    def read(cls):
        return Author.listar()

    @classmethod
    def verificar_autor(cls,autor):
        return Author.verify_id(autor)

class ControladorEditorial:

    @classmethod
    def create(cls, nombre):
        cls.editorial = Editorial(nombre)
        cls.editorial.insert_editorial()

    @classmethod
    def read(cls):
        return Editorial.listar()


class ControladorLector:

    @classmethod
    def create(cls, identificador,nombre):
        Usuario = User(identificador,nombre)
        Usuario.insert_user()
        print(f"Se registro al usuario {nombre} exitosamente")

    @classmethod
    def verify_unique_id(cls, identificador):
        return User.verify_id(identificador)

    @classmethod
    def verify_id_exists(cls, identificador):
        return User.verify_id_exists(identificador) 

    @classmethod
    def read(cls):
        return User.listar()


class ControladorLibro:

    @classmethod
    def verificar_id(cls,identificador):
        return Libro.verify_id(identificador)

    @classmethod
    def create(cls, identificador, nombre, autor, editorial):
        libro = Libro(identificador, nombre, autor, editorial)
        libro.insert_book()
        print(f'Se registro correctamente el libro {nombre}')

    @classmethod
    def verificar_editorial(cls,editorial):
        return Editorial.obtener_ids(editorial)



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