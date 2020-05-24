from database.connection import Conexion

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
    def __init__(self, sobrenombre, editorial, autor, nombre, disponible):
        self.sobrenombre = sobrenombre
        self.editorial = editorial
        self.autor = autor
        self.nombre = nombre
        self.disponible = disponible

    def insert_book(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO books (identifier,book, author_id, p_company_id, status) values (%(identifier)s, %(book)s, %(author_id)s, %(p_company_id)s, %(status)s);",{ 
            'identifier' : self.sobrenombre,
            'book': self.nombre,
            'author_id': self.autor,
            'p_company_id': self.editorial,
            'status': self.disponible
        })
        conn.connection.commit()
        conn.connection.close()