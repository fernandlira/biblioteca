from connection import Conexion

con = Conexion()

# Tabla usuarios
def create_users_table():
    query = "CREATE TABLE IF NOT EXISTS users (id SERIAL,identifier VARCHAR(15) NOT NULL UNIQUE,name VARCHAR(50) NOT NULL, PRIMARY KEY(identifier));"
    con.query(query)

# Tabla de Autores
def create_authors_table():
    query = "CREATE TABLE IF NOT EXISTS authors (id SERIAL UNIQUE,author VARCHAR(50) NOT NULL, PRIMARY KEY(id));"
    con.query(query)

# Tabla de Editoriales
def create_p_company_table():
    query = "CREATE TABLE IF NOT EXISTS p_companies (id SERIAL UNIQUE,p_company VARCHAR(50) NOT NULL, PRIMARY KEY(id));"
    con.query(query)

# Tabla Libros
def create_books_table():
    query = '''CREATE TABLE IF NOT EXISTS books (
        id SERIAL,
        identifier VARCHAR(15) NOT NULL UNIQUE, 
        book VARCHAR(50) NOT NULL,
        author_id int NOT NULL,
        p_company_id int NOT NULL,
        status boolean NOT NULL DEFAULT TRUE,
        PRIMARY KEY(identifier),
        FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE,
        FOREIGN KEY (p_company_id) REFERENCES p_companies(id) ON DELETE CASCADE
         );'''
    con.query(query)

# Tabla Alquiler
def create_borrows_table():
    query = '''CREATE TABLE IF NOT EXISTS borrows (id SERIAL UNIQUE,book_id VARCHAR(50) NOT NULL, user_id VARCHAR(50) NOT NULL, date DATE NOT NULL, date_of_return DATE NULL,
    FOREIGN KEY (book_id) REFERENCES books(identifier) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(identifier) ON DELETE CASCADE 
    );'''
    con.query(query)

def main():
    create_users_table()
    create_authors_table()
    create_p_company_table()
    create_books_table()
    create_borrows_table()
    con.close()

main()
