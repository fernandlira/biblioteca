import os
from psycopg2 import connect, Error
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


class Conexion:
    def __init__(self):
        try:
            self.connection = connect(user = os.getenv('DB_USER'),
                                        password = os.getenv('DB_PASSWORD'),
                                        host = os.getenv('DB_HOST'),
                                        port = os.getenv('DB_PORT'),
                                        database = os.getenv('DB_NAME')
                                        )

        except (Exception, Error) as error :
            print ("Error conectando a la BD", error)

    def query(self, query):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error :
            print ("Error:", error)
        

    def close(self):
        self.connection.commit()
        #self.cursor.close()
        self.connection.close()
