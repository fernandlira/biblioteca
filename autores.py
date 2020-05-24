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
        conn.query(f"SELECT * FROM authors")
        response = conn.cursor.fetchall()
        for r in response:
            print(f"ID: {r[0]} \nNombre: {r[1]}")

    def obtener_ids():
        ids = []
        conn = Conexion()
        conn.query(f"SELECT * FROM authors")
        response = conn.cursor.fetchall()
        for r in response:
            ids.append(r[0])
        return ids



