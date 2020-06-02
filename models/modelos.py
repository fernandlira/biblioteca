from database.connection import Conexion
from datetime import date

# Los modelos estan basados en las tablas en postgresSQL

# Tabla author
class Author:
    def __init__(self, author):
        self.author = author

# insertar autores en la tabla authors la bd
    def insert_author(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO authors (author) values (%(author)s);",{ 
            'author' : self.author
        })
        conn.connection.commit()
        conn.connection.close()

# listar datos de la tabla authors
    def listar():
        conn = Conexion()
        conn.query("SELECT * FROM authors")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"\nID: {r[0]} Nombre: {r[1]}\n")

# verificar a los autores
    def verify_id(identifier):
        ids = []
        conn = Conexion()
        conn.query(f"SELECT id FROM authors")
        response = conn.cursor.fetchall()
        for r in response:
            ids.append(r[0])
        if identifier in ids:
            return True

# Tabla p_companies
class Editorial:
    def __init__(self, editorial):
        self.editorial = editorial

# insertar datos en la tabla p_companies
    def insert_editorial(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO p_companies (p_company) values (%(p_company)s);",{ 
            'p_company' : self.editorial
        })
        conn.connection.commit()
        conn.connection.close()

# listar los datos de la tabla
    def listar():
        conn = Conexion()
        conn.query("SELECT * FROM p_companies")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"\nID: {r[0]} Nombre: {r[1]}\n")
    
# verificar los ids
    def obtener_ids(identifier):
        ids = []
        conn = Conexion()
        conn.query(f"SELECT * FROM p_companies")
        response = conn.cursor.fetchall()
        for r in response:
            ids.append(r[0])
        if identifier in ids:
            return True

# Tabla books y Borrows
class Libro:
    def __init__(self, identificador, nombre, autor, editorial):
        self.identificador = identificador
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial

# Insercion de libros
    def insert(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO books (identifier, book, author_id, p_company_id) values (%(identifier)s, %(book)s, %(author_id)s, %(p_company_id)s);",{ 
            'identifier' : self.identificador,
            'book': self.nombre,
            'author_id': self.autor,
            'p_company_id': self.editorial
        })
        conn.connection.commit()
        conn.connection.close()

# Listado de libros general
    def listar():
        conn = Conexion()
        conn.query("SELECT identifier, book, author, p_company from books as b inner join authors as a on b.author_id =a.id inner join p_companies as e on b.p_company_id = e.id;")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"\ISBN: {r[0]} Libro: {r[1]} Autor: {r[2]} Editorial: {r[3]}\n")

# Listar libros disponibles
    def listar_disponibles():
        conn = Conexion()
        conn.query("SELECT * FROM books WHERE status = True")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nIdentificador: {r[1]} \nNombre: {r[2]}\nAutor: {r[3]}\nEditorial: {r[4]}\n")

# Identificador de libros pero identifica el ISBN
    def verify_id(identifier):
        lista = []
        conn = Conexion()
        conn.query("SELECT * FROM books")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[1])
        if identifier not in lista:
            return True

# Aca verifica solo los ISBN de los libros que esten en status TRUE
    def alquiler_verify_id(identifier):
        lista = []
        conn = Conexion()
        conn.query("SELECT identifier FROM books WHERE status = True")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[0])
        if identifier in lista:
            return True

# verificacion de libros cuando estan en status FALSE
    def verify_if_borrowed(identifier):
        lista = []
        conn = Conexion()
        conn.query("SELECT identifier FROM books WHERE status = False")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[0])
        if identifier in lista:
            return True

# Insersion de datos en la tabla BORROWS
    @staticmethod
    def borrow_book(book_id,author_id):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO borrows (book_id,user_id,date) values (%(book_id)s, %(user_id)s, %(date)s);",{ 
            'book_id' : book_id,
            'user_id': author_id,
            'date': date.today()
        })
        conn.connection.commit()
        cursor.execute(f"UPDATE books SET status = False WHERE identifier = (%(book_id)s);",{ 
            'book_id' : book_id
        })
        conn.connection.commit()
        conn.connection.close()

# Actualizado en devolucion del libro en la tabla borrows
    @staticmethod
    def devolver(book_id):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"UPDATE borrows set date_of_return = (%(date)s) WHERE book_id = (%(book_id)s) AND id IN(SELECT max(id) FROM borrows);",{ 
            'book_id' : book_id,
            'date': date.today()
        })
        conn.connection.commit()
        cursor.execute(f"UPDATE books SET status = True WHERE identifier = (%(book_id)s);",{ 
            'book_id' : book_id
        })
        conn.connection.commit()
        conn.connection.close()

# Eliminacion de libros en la tabla BOOKS
    @staticmethod
    def eliminar_libro(identificador):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"DELETE FROM books WHERE identifier = (%(identifier)s)",{ 
            'identifier' : identificador
        })
        conn.connection.commit()
        conn.connection.close()

#  listado en la tabla BORROWS
    def listar_borrow():
        conn = Conexion()
        conn.query("SELECT p.identifier, book, user_id, name, date, date_of_return from borrows as b inner join books as p on b.book_id=p.identifier inner join users as u on b.user_id = u.identifier WHERE date_of_return = Null")
        response = conn.cursor.fetchall()
        for r in response:
            print(f'\nISBN: {r[0]}, libro: {r[1]}, DNI: {r[2]}, Lector: {r[3]}, Fecha Préstamo: {r[4]}, Fecha Devolución: {r[5]}\n')    

# Tabla Users
class User:
    def __init__(self,identifier,name):
        self.identifier = identifier
        self.name = name
 
# inserta usuarios a la tabla users
    def insert_user(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO users (identifier,name) values (%(identifier)s,%(name)s);",{ 
            'identifier' : self.identifier,
            'name' : self.name
        })
        conn.connection.commit()
        conn.connection.close()

# verifica los identificadores de la tabla no estan en la lista
    def verify_id(identifier):
        lista = []
        conn = Conexion()
        conn.query("SELECT * FROM users")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[1])
        if identifier not in lista:
            return True

# verifica los identificadores si existen
    def verify_id_exists(identifier):
        lista = []
        conn = Conexion()
        conn.query("SELECT * FROM users")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[1])
        if identifier in lista:
            return True

# lista los usuarios de la tabla users
    def listar():
        conn = Conexion()
        conn.query("SELECT * FROM users")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nIdentificador: {r[1]} \nNombre: {r[2]}\n")

    def __str__(self):
        return f"\nIdentificador: {self.identifier}, Nombre: {self.name}\n"