from models.modelos import (Author, Libro, Alquiler, User)

class ControladorAutor:

    @classmethod
    def registrar_autor(cls, nombre):
        Autor = Author(nombre)
        Autor.insert_author()
        print(f"Se registro al autor {nombre} exitosamente")

    @classmethod
    def listar_autores(cls):
        return Author.listar()

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

class ControladorBook:

    libros = []

    @classmethod
    def registrar_libro(cls, datos_libro):
        if cls.libros is None:
            cls.libros = []
        nuevo_libro = Libro(
            datos_libro['nombre'],
            datos_libro['author']
        )
        cls.libros.append(nuevo_libro)
        return  nuevo_libro

class ControladorAlquiler:
    
    alquiler = None
    alquiler_nuevo = None

    @classmethod
    def registrar_alquiler(cls, datos_lector):
        if cls.alquiler is None:
            cls.alquiler = []
        cls.alquiler.append(
            Alquiler(
                datos_lector['dni'],
                datos_lector['lector']
            )
        )
        cls.alquiler_nuevo = cls.alquiler[-1]
        return cls.alquiler_nuevo

    @classmethod
    def registrar_libro_a_lector(cls, nombre_libro, fecha_hoy, fecha_entrega):
        response = False
        libro_alquilado = Libro.buscar_libro(
            nombre_libro, ControladorBook.libros
        )
        if libro_alquilado:
            cls.alquiler_nuevo.añadir_libros(
                libro_alquilado, fecha_hoy, fecha_entrega
            )
            response = True
        return response