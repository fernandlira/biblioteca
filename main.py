from database.connection import Conexion
from classes.libreria import (Author, P_company, Books, User)

def registrarLibro():
    try:
        while True:
            try:
                idenficador = input("Ingresa el identificador del nuevo libro: ")
                if idenficador.upper() not in Books.get_identifiers_list():
                    break
                else:
                    raise Exception("--- Ya existe el identificador --- Por favor, ingrese uno diferente")
            except Exception as e:
                print(f"error aqui: {str(e)}")
        while True:
                P_company.listar()
                while True:
                    try:
                        editorial = int(input("Ingrese el ID de la editorial: "))
                        if editorial in P_company.obtener_ids():
                            break
                        else:
                            raise Exception("El ID del editorial no existe")
                    except Exception as e:
                        print(f"str{e}")
                
                while True:
                    Author.listar()
                    try:
                        author = int(input("Ingrese el ID del autor: "))
                        if author in Author.obtener_ids():
                            break
                        else:
                            raise Exception("El ID del autor no existe")
                    except Exception as e:
                        print(f"error aqui: {str(e)}")

                libro = input(f'Ingrese el nombre del libro: ')
                nuevo = Books(idenficador, editorial, author, libro)
                nuevo.insert_book()
                break
    except Exception as e:
        print(f"Error aqui: {str(e)}")
    except KeyboardInterrupt:
        print('se interrumpio la app')
    except ValueError:
        print('No puso un dato')

def incribirLector():
    try:
        while True:
            try:
                idenficador = input("Ingresa el identificador del nuevo lector: ")
                if idenficador.upper() not in User.get_identifiers_list():
                    break
                else:
                    raise Exception("--- Ya existe el identificador --- Por favor, ingrese uno diferente")
            except Exception as e:
                print(f"error aqui: {str(e)}")
        lector = User(idenficador.upper(),input("Ingrese el nombre del nuevo lector: "))
        lector.insert_user()
    except Exception as i:
        print('Error aqui:', str(i))
    except KeyboardInterrupt:
        print('Se interrumpio la app')

def alquilarLibros():
    User.listar()
    try:
        while True:
            try:
                u_idenficador = input("Ingresa el identificador del lector: ")
                if u_idenficador.upper() in User.get_identifiers_list():
                    print("")
                    break
                else:
                    raise Exception("--- EL identificador no existe --- Por favor, ingrese uno diferente")
            except Exception as e:
                print(f"error aqui: {str(e)}")
        Books.listar_alquiler()
        ids = [] 
        while True:
            while True:
                try:
                    id_libro = input("Ingresa el codigo del libro: ")
                    if id_libro.upper() in Books.get_identifiers_list2():
                        ids.append(id_libro)
                        break
                    else:
                        raise Exception("--- EL identificador no existe o no esta disponible --- Por favor, ingrese uno diferente")
                except Exception as i:
                    print('Error aqui:', str(i))
            opcion = int(input("¿Desea alquilar otro libro? (0) NO (1) SI: "))
            if opcion == 0:
                break
        for ide in ids:
            Books.borrow_book(ide,u_idenficador)
            print(f"Alquiler del libro {ide} completado!")
        
        
    except Exception as i:
        print('Error aqui:', str(i))
    except KeyboardInterrupt:
        print('Se interrumpio la app')

def main():
    while True:
        print('BIENVENIDO A LA BIBLIOTECA!')
        print('(1) Registrar nuevo Libro (2) Agregar Nueva Editorial (3) Agregar Nuevo Autor (4) Inscribir Lector')
        print('(5) Listar Lectores (6) Listar Libros (7) Alquilar Libros (0) Salir')
        opcion = int(input('Ingrese la opción: '))
        if opcion == 0:
            break
        elif opcion == 1:
            registrarLibro()
        elif opcion == 2:
            editorial = P_company(input("Inserta nombre de editorial: "))
            editorial.insert_editorial()
        elif opcion == 3:
            autor = Author(input("Inserta nombre de Autor: "))
            autor.insert_author()
        elif opcion == 4:
            incribirLector()
        elif opcion == 5:
            User.listar()
        elif opcion == 6:
            Books.listar()
        elif opcion == 7:
            alquilarLibros()
                 

main()