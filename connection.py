import psycopg2

class Conexion:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(user = "postgres",
                                        password = "liraq_07",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "library")

        except (Exception, psycopg2.Error) as error :
            print ("Error conectando a la BD", error)

    def query(self, query):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error :
            print ("Error:", error)
        

    def close(self):
        self.cursor.close()
        self.connection.close()
