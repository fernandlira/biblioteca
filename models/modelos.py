class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"\nLibreria : {self.nombre}\n"

class Libro:
    def __init__(self, nombre, author):
        self.nombre = nombre
        self.author = author

    @staticmethod
    def buscar_libro(nombre, libros):
        resultado = None
        for libro in libros:
            if libro.nombre == nombre:
                resultado = libro
                break
        return resultado

    def __str__(self):
        return (
            "\n----------LIBRO-------------\n"
            f"\n Nombre del libro : {self.nombre}\n"
            f"\n nombre del author : {self.author}\n"
            "\n----------------------------\n"
            )

class Alquiler:
    def __init__(self, dni, lector):
        self.dni = dni
        self.lector = lector
        self.prestamo = []

    def añadir_libros(self, libro, fecha_hoy, fecha_entrega):
        self.prestamo.append(
            (libro, fecha_hoy, fecha_entrega)
        )

    def __str__(self):
        return (
            "\n---------------------------------------"
            f"\nSu DNI: {self.dni}\n"
            f"\nla persona: {self.lector}\n"
            f"\ndetalle: {self.prestamo}\n"
            "------------------------------------------"
        )
