from controllers.controladores import (
    ControladorAuthor, ControladorEditorial
    )

class vistaAuthor:

    @staticmethod
    def ingreso_author():
        if ControladorAuthor.author is None:
            nombre = input('ingrese el nombre del autor: ')
            ControladorAuthor.registrar_author(
                {
                    'nombre': nombre
                }
            )
        else:
            print('Ya se registro el autor')
        print(ControladorAuthor.author)

class vistaEditorial:

    @staticmethod
    def ingreso_editorial():
        if ControladorEditorial.editorial is None:
            nombre = input('ingrese el nombre de la editorial: ')
            ControladorEditorial.registrar_editorial(
                {
                    'nombre': nombre
                }
            )
        else:
            print('Ya se registro la editorial')
        print(ControladorEditorial.editorial)


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
        opcion = int(input('escriba la opcion: '))

        if opcion == 1:
            vistaAuthor.ingreso_author()
        elif opcion == 2:
            vistaEditorial.ingreso_editorial()