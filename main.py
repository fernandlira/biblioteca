from database.connection import Conexion

def inserLibros():
    try:
        nro_editorial = int(input('ingrese el nro de editoriales: '))
        a = 1
        while True:
            try:
                editorial = str(input(f'ingrese el nombre de la editorial nro{a}: '))
                nro_libros = int(input(f'ingrese el numero de libros: '))
                b = 1
                while True:
                    try:
                        autores = []
                        libro = str(input(f'ingrese el nombre del libro Nr°{b}: '))
                        autor = str(input('ingrese el nombre del autor: '))
                        disponible = input('esta disponible?: ')
                        b += 1
                        if b > nro_libros:
                            break
                    except ValueError:
                        print('olvidaste ingresar algo')
                a += 1
                if a > nro_editorial:
                    break
            except ValueError:
                print('no ingresaste un dato')
    except ValueError:
        print('no ingresaste un dato')
    except KeyboardInterrupt:
        print('se detubo la app')
    except Exception as a:
        print(f'ocurrio un error aqui: {str(a)}')

inserLibros()