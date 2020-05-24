from database.connection import Conexion

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


