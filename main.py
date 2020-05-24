from database.connection import Conexion
from classes.libreria import (Author, P_company, Books, User)

def registrarLibro():
    try:
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
                disponible = input('escriba True si esta disponible: ')
                apodo = input('ingresa un sobrenombre: ')
                nuevo = Books(apodo, editorial, author, libro, disponible)
                nuevo.insert_book()
                break


    except Exception as e:
        print(f"Error aqui: {str(e)}")
    except KeyboardInterrupt:
        print('se interrumpio la app')
    except ValueError:
        print('No puso un dato')



def main():
    while True:
        print('BIENVENIDO A LA BIBLIOTECA!')
        print('(1) Registrar nuevo Libro (2) Agregar Nueva Editorial (3) Agregar Nuevo Autor (4) Inscribir Lector')
        print('(5) Listar Lectores (0) Salir')
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
            while True:
                try:
                    idenficador = input("Ingresa el identificador del nuevo lector: ")
                    if idenficador.upper() not in User.get_identifiers_list():
                        break
                    else:
                        raise Exception("--- Ya existe el identificador --- Por favor, ingrese uno diferente")
                except Exception as e:
                    print(f"{e}")
            lector = User(idenficador.upper(),input("Ingrese el nombre del nuevo lector: "))
            lector.insert_user()
        elif opcion == 5:
            User.listar()
                 

        
main()