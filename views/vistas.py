from controllers.controladores import (
    ControladorAuthor, ControladorEditorial, ControladorLibro
    )
from models.modelos import (
    Author, P_company, Books
    )

class VistaAuthor:

    @staticmethod
    def ingreso_author():
        if ControladorAuthor.author is None:
            nombre = input('ingrese el nombre del autor: ')
            ControladorAuthor.registrar_author(
                {
                    'nombre': nombre
                }
            )
            a = Author(nombre)
            a.insert_author()
        else:
            print('Ya se registro el autor')
        print(ControladorAuthor.author)

class VistaEditorial:

    @staticmethod
    def ingreso_editorial():
        if ControladorEditorial.editorial is None:
            nombre = input('ingrese el nombre de la editorial: ')
            ControladorEditorial.registrar_editorial(
                {
                    'nombre': nombre
                }
            )
            p = P_company(nombre)
            p.insert_editorial()
        else:
            print('Ya se registro la editorial')
        print(ControladorEditorial.editorial)

class VistaBook:

    @staticmethod
    def ingreso_libro():
        if ControladorLibro.book is None:
            idenficador = input("Ingresa un apodo para el nuevo libro: ")
            P_company.listar()
            editorial = int(input("Ingrese el ID de la editorial: "))
            Author.listar()
            author = int(input("Ingrese el ID del autor: "))
            libro = input('Ingrese el nombre del libro: ')
            ControladorLibro.registrarLibro(
                {
                    'identifier': idenficador,
                    'p_company_id': editorial,
                    'author_id': author,
                    'book': libro
                }
            )
            b = Books(idenficador, editorial, author, libro)
            b.insert_book()
        else:
            print('Ya se ingreso un libro!')
        print(ControladorLibro.book)

    def vista_libro():
        Books.listar()
class vistaAplicacion:
    @staticmethod
    def iniciar():
        vistaAplicacion.bienvenida()
        vistaAplicacion.menu()

    @staticmethod
    def bienvenida():
        print('BIENVENIDO A LA BIBLIOTECA!')

    @staticmethod
    def menu():
        print('Escriba 1 para registrar un author: ')
        print('Escriba 2 para registrar una editorial: ')
        print('Escriba 3 para Registrar un Libro')
        print('Escriba 4 para Listar los libros que estan en la biblioteca')
        opcion = int(input('escriba la opcion: '))
        if opcion == 1:
            VistaAuthor.ingreso_author()
        elif opcion == 2:
            VistaEditorial.ingreso_editorial()
        elif opcion == 3:
            VistaBook.ingreso_libro()
        elif opcion == 4:
            VistaBook.vista_libro()