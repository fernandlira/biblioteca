from controllers.controlador import (ControladorAutor, ControladorEditorial, ControladorLibro, ControladorLector, ControladorAlquiler)

# creaciones de vistas para ejecutar los imputs y prints

# vista para los usuarios
class VistaLector:

# menu de la zona de lectores
    @staticmethod
    def menu():
        while True:
            print('\n')
            print('ESTAS EN LA SECCION DE LECTORES')
            print('(1) Registrar Lector (2) Listar Lectores (3) Para retroceder al menu principal')
            opcion = int(input('Ingrese la opción: '))
            if opcion == 1:
                VistaLector.registro()
            elif opcion == 2:
                ControladorLector.read()
            else:
                break

# registro de usuarios lectores
    @staticmethod
    def registro():
        while True:
            try:
                identificador = input("Ingresa su identificador: ")
                if ControladorLector.verify_unique_id(identificador.upper()):
                    break
                else:
                    raise Exception("--- Ya existe el identificador --- Por favor, ingrese uno diferente")
            except Exception as e:
                print(f"error aqui: {str(e)}")
        ControladorLector.create(identificador.upper(),input("Ingrese el nombre del nuevo lector: "))

# vista para los libros
class VistaLibro:

# La vista del menu de libros 
    @staticmethod
    def menu():
        while True:
            print('\n')
            print('ESTAS EN LA SECCION DE REGISTRO DE LIBROS')
            print('(1) Registrar Autor (2) Registrar Editorial (3) Registrar Libro (4) Ver libros (5) Eliminar libro (7) Para regresar al menu principal')
            opcion = int(input('ingrese el numero: '))
            if opcion == 1:
                VistaLibro.ingreso_autor()
            elif opcion == 2:
                VistaLibro.ingreso_editorial()
            elif opcion == 3:
                VistaLibro.ingreso_libro()
            elif opcion == 4:
                VistaLibro.listar_libros()
            elif opcion == 5:
                VistaLibro.eliminar_libro()
            else:
                break

#  el ingreso del nombre del autor
    @staticmethod
    def ingreso_autor():
        nombre = input("Ingrese nombre de Autor: ")
        ControladorAutor.create(nombre)

# el ingreso de la editorial
    @staticmethod
    def ingreso_editorial():
        nombre = input('Ingrese nombre de editorial: ')
        ControladorEditorial.create(nombre)

# el listado de libros
    @staticmethod
    def listar_libros():
        ControladorLibro.read()

# el ingreso de libros
    @staticmethod
    def ingreso_libro():
        try:
            while True:
                try:
                    identificador = input("Ingresa el ISBN del Libro: ").upper()
                    if ControladorLibro.verificar_id(identificador):
                        break
                    else:
                        raise Exception("--- Ya existe el ISBN --- Por favor, ingrese uno diferente")
                except Exception as e:
                    print(f"error aqui: {str(e)}")
            libro = input('Ingrese el nombre del libro: ')
            while True:
                    VistaLibro.lista_editoriales()
                    while True:
                        try:
                            editorial = int(input("Ingrese el ID de la editorial: "))
                            if ControladorLibro.verificar_editorial(editorial):
                                break
                            else:
                                raise Exception("El ID del editorial no existe, ingrese uno de la lista")
                        except Exception as e:
                            print(f"Error aqui: {str(e)}")
                    
                    while True:
                        VistaLibro.listado_autores()
                        try:
                            autor = int(input("Ingrese el ID del autor: "))
                            if ControladorAutor.verificar_autor(autor):
                                break
                            else:
                                raise Exception("El ID del autor no existe, ingrese uno de la lista")
                        except Exception as e:
                            print(f"{e}")
                    ControladorLibro.create(identificador.upper(), libro, autor, editorial)
                    break
        except Exception as e:
            print(f"Error aqui: {str(e)}")
        except KeyboardInterrupt:
            print('se interrumpio la app')
        except ValueError:
            print('No puso un dato')

# el listado de autores
    @staticmethod
    def listado_autores():
        return ControladorAutor.read()

# el listado de editoriales
    @staticmethod
    def lista_editoriales():
        return ControladorEditorial.read()

# la funcion de eliminar libros
    @staticmethod
    def eliminar_libro():
        try:
            VistaLibro.listar_libros()
            isbn = input('ingrese el ISBN del libro que desea borrar: ')
            ControladorLibro.eliminar_libro(isbn)
            print('\nEliminado satisfactoriamente\n')
        except ValueError:
            print('no pusiste un dato')

# vistas para los alquileres
class BorrowBook:

# el menu del alquilar libros
    @staticmethod
    def menu():
        print('(1) Alquilar un Libro (2) Devolver un libro (3) Listar Alquileres')
        opcion = int(input('Ingrese la opción: '))
        if opcion == 1:
            BorrowBook.borrow_book()
        elif opcion == 2:
            BorrowBook.return_book()
        elif opcion == 3:
            ControladorAlquiler.read()

# ingreso del usuario lector y el libro que desea alquilar
    @staticmethod
    def borrow_book():
        ControladorLector.read()
        try:
            while True:
                try:
                    u_idenficador = input("Ingresa el identificador del lector: ").upper()
                    if ControladorLector.verify_id_exists(u_idenficador):
                        print("")
                        break
                    else:
                        raise Exception("--- EL identificador no existe --- Por favor, ingrese uno diferente")
                except Exception as e:
                    print(f"error aqui: {str(e)}")
            ControladorLibro.listar_libros_disponibles()
            ids = []
            while True:
                while True:
                    try:
                        id_libro = input("Ingresa el codigo del libro: ").upper()
                        if ControladorAlquiler.verificar_id(id_libro):
                            ids.append(id_libro)
                            break
                        else:
                            raise Exception("--- EL identificador no existe o no esta disponible --- Por favor, ingrese uno diferente")
                    except Exception as i:
                        print('Error aqui:', str(i))
                opcion = int(input("¿Desea alquilar otro libro? (0) NO (1) SI: "))
                if opcion == 0:
                    break
            ControladorAlquiler.borrow(list(set(ids)),u_idenficador)
                                  
        except Exception as i:
            print('Error aqui:', str(i))
        except KeyboardInterrupt:
            print('Se interrumpio la app')

# funcion de retornar el libro alquilado
    @staticmethod
    def return_book():
        try:
            while True:
                try:
                    BorrowBook.borrow_list()
                    idenficador = input("Ingresa el ISBN del libro a devolver: ").upper()
                    if ControladorLibro.verificar_libros_alquilados(idenficador):
                        ControladorLibro.devolver(idenficador)
                        print("Devolucion exitosa!")
                        break
                    else:
                        raise Exception("--- EL identificador no existe o no pertenece a un libro alquilado --- Por favor, ingrese uno diferente")
                except Exception as e:
                    print(f"error aqui: {str(e)}")
                                  
        except Exception as i:
            print('Error aqui:', str(i))
        except KeyboardInterrupt:
            print('Se interrumpio la app')

# lista de libros alquilados
    def borrow_list():
        return ControladorAlquiler.read()

# vista para la aplicacion se ejecute
class VistaAplicacion:
# vista que ejecuta las funciones principales de la aplicacion
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
            print('Se detuvo la app')

# funcion de bienvenida
    @staticmethod
    def bienvenida():
        print('BIENVENIDO')

# vista del menu principal
    @staticmethod
    def menu():
        while True:
            print('(1) Accede al Menú de Libros (2) Accede al Menú de Lectores (3) Accede al Menú de alquiler  ')
            opcion = int(input('Ingresa la opción: '))
            if opcion == 1:
                VistaLibro.menu()
            elif opcion == 2:
                VistaLector.menu()
            elif opcion == 3:
                BorrowBook.menu()
            else:
                break