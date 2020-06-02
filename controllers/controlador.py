from models.modelos import (Author, Editorial, Libro, User)

# Controlador que uno los modelos con las vistas

# controlador del autor
class ControladorAutor:
# crear autores
    @classmethod
    def create(cls, nombre):
        cls.autor = Author(nombre)
        cls.autor.insert_author()
        print(f"Se registro al autor {nombre} exitosamente")

# leer cada autor que este en la tabla authors
    @classmethod
    def read(cls):
        return Author.listar()

# verificar autor por el nombre
    @classmethod
    def verificar_autor(cls,autor):
        return Author.verify_id(autor)

# Controlador de editorial
class ControladorEditorial:

# crear editorial
    @classmethod
    def create(cls, nombre):
        cls.editorial = Editorial(nombre)
        cls.editorial.insert_editorial()

# leer lista de editoriales 
    @classmethod
    def read(cls):
        return Editorial.listar()

# Controlador de los usuarios
class ControladorLector:

# creacion del usuario
    @classmethod
    def create(cls, identificador,nombre):
        Usuario = User(identificador,nombre)
        Usuario.insert_user()
        print(f"Se registro al usuario {nombre} exitosamente")

# verificador de ifentificador del usuario
    @classmethod
    def verify_unique_id(cls, identificador):
        return User.verify_id(identificador)

# verificaion de usuarios
    @classmethod
    def verify_id_exists(cls, identificador):
        return User.verify_id_exists(identificador) 

# listado de usuarios
    @classmethod
    def read(cls):
        return User.listar()

# Controlador de libros
class ControladorLibro:

# Insertar libros a la base de datos
    @classmethod
    def create(cls, identificador, nombre, autor, editorial):
        libro = Libro(identificador, nombre, autor, editorial)
        libro.insert()
        print(f'Se registro correctamente el libro {nombre}')

# verificar libros tomando su ISBN
    @classmethod
    def verificar_id(cls,identificador):
        return Libro.verify_id(identificador)

# verificar editorial si existe realmente
    @classmethod
    def verificar_editorial(cls,editorial):
        return Editorial.obtener_ids(editorial)

# Verificar libros cuando estan en status false
    @classmethod
    def verificar_libros_alquilados(cls,identifier):
        return Libro.verify_if_borrowed(identifier)

# Listar libros
    @classmethod
    def read(cls):
        return Libro.listar()

# listar libros disponibles
    @classmethod
    def listar_libros_disponibles(cls):
        return Libro.listar_disponibles()

# Retornar el libro a la biblioteca
    @classmethod
    def devolver(cls,identifier):
        return Libro.devolver(identifier)

# Funcion ELiminar
    @classmethod
    def eliminar_libro(cls, identificador):
        return Libro.eliminar_libro(identificador)

# Controlador del alquiler de libros
class ControladorAlquiler:

# verificar los ids
    @classmethod
    def verificar_id(cls,identificador):
        return Libro.alquiler_verify_id(identificador)

# insertar libros a la tabla de borrows
    @classmethod
    def borrow(cls,ids,u_idenficador):
        for ide in ids:
            Libro.borrow_book(ide,u_idenficador)
            print(f"Alquiler del libro {ide} completado!")

# leer los lista de libros de la tabla borrows
    @classmethod
    def read(cls):
        return Libro.listar_borrow()