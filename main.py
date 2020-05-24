from database.connection import Conexion
from editorial import P_company
from autores import Author

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
                        print(f"str{e}")

                libro = input(f'Ingrese el nombre del libro: ')
                disponible = True
                #libro = Libro(libro, editorial, autor, disponible)
                break

                #libro = Libro(libro, editorial, autor, disponible)
                #libro.insertar()
    except Exception as e:
        print(f"str{e}")



def main():
    print('BIENVENIDO A LA BIBLIOTECA!')
    print('presiona 1 si deseas regristrar libros o 2 si deseas ingresar editorial o 3 si deseas ingresar autor')
    opcion = int(input('ingrese el numero: '))
    if opcion == 1:
        registrarLibro()
    if opcion == 2:
        editorial = P_company(input("Inserta nombre de editorial: "))
        editorial.insert_editorial()
    if opcion == 3:
        autor = Author(input("Inserta nombre de Autor: "))
        autor.insert_author()
        
main()