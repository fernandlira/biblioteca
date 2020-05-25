from database.connection import Conexion

class Author:
    def __init__(self, author):
        self.author = author

    def insert_author(self):
        conn = Conexion()
        cursor = conn.connection.cursor()
        cursor.execute(f"INSERT INTO authors (author) values (%(author)s);",{ 
            'author' : self.author
        })
        conn.connection.commit()
        conn.connection.close()

    def __str__(self):
        return f"\nAuthor : {self.author}\n"

class P_company:
    def __init__(self, editorial):
        self.editorial = editorial

    def __str__(self):
        return f"\nEditorial : {self.editorial}\n"


class Books:
    def __init__(self, sobrenombre, editorial, autor, nombre, disponible):
        self.sobrenombre = sobrenombre
        self.editorial = editorial
        self.autor = autor
        self.nombre = nombre
        self.disponible = disponible

    def __str__(self):
        return f"\nLibro: {self.nombre}, Disponible: {self.disponible}\n"