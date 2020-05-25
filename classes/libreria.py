from database.connection import Conexion
from datetime import datetime

class Author:
    def __init__(self,author):
        self.author = author

    def insert_author(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO authors (author) values (%(author)s);",{ 
            'author' : self.author
        })
        conn.connection.commit()
        conn.connection.close()
        print(f"Se ha registrado al autor: {self.author}")
    
    def listar():
        conn = Conexion()
        conn.query("SELECT * FROM authors")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nNombre: {r[1]}")

    def obtener_ids():
        ids = []
        conn = Conexion()
        conn.query("SELECT * FROM authors")
        response = conn.cursor.fetchall()
        for r in response:
            ids.append(r[0])
        return ids

class P_company:
    def __init__(self,editorial):
        self.editorial = editorial

    def insert_editorial(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO p_companies (p_company) values (%(p_company)s);",{ 
            'p_company' : self.editorial
        })
        conn.connection.commit()
        conn.connection.close()
    
    def listar():
        conn = Conexion()
        conn.query(f"SELECT * FROM p_companies")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nNombre: {r[1]}")

    def obtener_ids():
        ids = []
        conn = Conexion()
        conn.query(f"SELECT * FROM p_companies")
        response = conn.cursor.fetchall()
        for r in response:
            ids.append(r[0])
        return ids


class Books:
    def __init__(self, sobrenombre, editorial, autor, nombre):
        self.sobrenombre = sobrenombre
        self.editorial = editorial
        self.autor = autor
        self.nombre = nombre

    def insert_book(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO books (identifier, book, author_id, p_company_id) values (%(identifier)s, %(book)s, %(author_id)s, %(p_company_id)s);",{ 
            'identifier' : self.sobrenombre,
            'book': self.nombre,
            'author_id': self.autor,
            'p_company_id': self.editorial
        })
        conn.connection.commit()
        conn.connection.close()

    def listar():
        conn = Conexion()
        conn.query("SELECT * FROM books")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nIdentificador: {r[1]} \nNombre: {r[2]}\nAutor: {r[3]}\nEditorial: {r[4]}")
            if r[5]:
                print("Disponible\n")
            else:
                print("No Disponible\n")

    def listar_alquiler():
        conn = Conexion()
        conn.query("SELECT * FROM books WHERE status = True")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nIdentificador: {r[1]} \nNombre: {r[2]}\nAutor: {r[3]}\nEditorial: {r[4]}\n")

    def get_identifiers_list():
        lista = []
        conn = Conexion()
        conn.query(f"SELECT * FROM books")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[1])
        return lista
    
    def get_identifiers_list2():
        lista = []
        conn = Conexion()
        conn.query(f"SELECT * FROM books WHERE status = True")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[1])
        return lista

    @staticmethod
    def borrow_book(book_id,author_id):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO borrows (book_id,user_id,date) values (%(book_id)s, %(user_id)s, %(date)s);",{ 
            'book_id' : book_id,
            'user_id': author_id,
            'date': datetime.today()
        })
        conn.connection.commit()
        cursor.execute(f"UPDATE books SET status = False WHERE identifier = (%(book_id)s);",{ 
            'book_id' : book_id
        })
        conn.connection.commit()
        conn.connection.close()


class User:
    def __init__(self,identifier,name):
        self.identifier = identifier
        self.name = name

    def insert_user(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO users (identifier,name) values (%(identifier)s,%(name)s);",{ 
            'identifier' : self.identifier,
            'name' : self.name
        })
        conn.connection.commit()
        conn.connection.close()

    def get_identifiers_list():
        lista = []
        conn = Conexion()
        conn.query(f"SELECT * FROM users")
        response = conn.cursor.fetchall()
        for r in response:
            lista.append(r[1])
        return lista

    def listar():
        conn = Conexion()
        conn.query("SELECT * FROM users")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nIdentificador: {r[1]} \nNombre: {r[2]}\n")
    
