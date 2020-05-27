from controllers.controlador import (ControladorLibreria, ControladorBook, ControladorAlquiler)

class VistaLibreria:

    @staticmethod
    def ingreso_libreria():
        if ControladorLibreria.libreria is None:
            nombre = input('ingrese el nombre de la Libreria: ')
            ControladorLibreria.registrar_libreria(
                {
                    'nombre': nombre
                }
            )
        print(ControladorLibreria.libreria)

class VistaBook:

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print('\n')
            print('ESTAS EN LA SECCION DE REGISTRO DE LIBROS')
            print('escriba 1 si desea crear un nuevo libro')
            print('escriba 2 si desea listar los libros')
            print('escriba 3 para regresar')
            opcion = int(input('ingrese el numero: '))
            if opcion == 1:
                VistaBook.ingreso_libro()
            elif opcion == 2:
                VistaBook.listar_libros()
            else:
                continuar = False

    @staticmethod
    def ingreso_libro():
        nombre = input('ingres el nombre del libro: ')
        author = input('ingrese el nombre del author: ')
        nuevo_libro = ControladorBook.registrar_libro(
            {
                'nombre': nombre, 'author': author
            }
        )
        print(nuevo_libro)

    @staticmethod
    def listar_libros():
        for b in ControladorBook.libros:
            print(b)

class VistaAlquiler:
    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print('\n')
            print('BIENVENIDO A LA SECCION DE ALQUILER DE LIBROS')
            print('QUE LIBRO DESEA ADQUIRIR?')
            print('presione 1 para adquirir un libro')
            print('escriba 2 para listar sus libros')
            print('escriba 3 para regresar')
            opcion = int(input('Ingrese un numero: '))
            if opcion == 1:
                VistaAlquiler.ingreso_alquiler()
            elif opcion == 2:
                VistaAlquiler._listar_libro()
            else:
                continuar = False

    @staticmethod
    def ingreso_alquiler():
        VistaAlquiler._ingreso_lector()
        VistaAlquiler._agregar_libro()

    @staticmethod
    def _ingreso_lector():
        nombre = input('Ingrese su nombre: ')
        dni = input('ingrese su DNI: ')
        nuevo_alquiler = ControladorAlquiler.registrar_alquiler(
            {
                'dni': dni,
                'lector': nombre
            }
        )
        print(f'\nBIENVENIDO: {nuevo_alquiler.lector}\n')

    @staticmethod
    def _agregar_libro():
        nombre_libro = input('Ingrese un libro de la libreria: ')
        fecha_de_hoy = input('Ingrese la fecha de hoy: ')
        fecha_de_entrega = input('Ingrese la fecha en el cual devolvera el libro: ')
        response = ControladorAlquiler.registrar_libro_a_lector(
            nombre_libro, fecha_de_hoy ,fecha_de_entrega
        )
        if response:
            print('Se añadio el libro')
        else:
            print('no se encontro el libro :(')

    @staticmethod
    def _listar_libro():
        for b in ControladorAlquiler.alquiler:
            print(b)


class VistaAplicacion:
    @staticmethod
    def iniciar():
        try:
            VistaAplicacion.bienvenida()
            VistaAplicacion.menu()
        except ValueError:
            print('no ingresaste un dato')
        except Exception as a:
            print(f'ocurrio un error aqui: {str(a)}')
        except KeyboardInterrupt:
            print('se detubo la app')

    @staticmethod
    def bienvenida():
        print('BIENVENIDO')

    @staticmethod
    def menu():
        continuar = True
        while continuar:
            print('Puedes Ingresar el nombre de la libreria escribiendo 1')
            print('PRIMERO REGISTRA NUEVOS LIBROS, para eso escribe 2')
            print('Para ingresar al menu de libros a Alquilar, escriba 3')
            opcion = int(input('ingresa el numero: '))
            if opcion == 1:
                VistaLibreria.ingreso_libreria()
            elif opcion == 2:
                VistaBook.menu()
            elif opcion == 3:
                VistaAlquiler.menu()
            else:
                continuar = False