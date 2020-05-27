from models.modelos import (Libreria, Libro, Alquiler)


class ControladorLibreria:

    libreria = None

    @classmethod
    def registrar_libreria(cls, datos_libreria):
        cls.libreria = Libreria(
            datos_libreria['nombre']
            )
        return cls.libreria

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