from models.modelos import (
    Author, P_company, Books
    )

class ControladorAuthor:

    author = None

    @classmethod
    def registrar_author(cls, datos_author):
        cls.author = Author(datos_author['nombre'])
        return cls.author


class ControladorEditorial:

    editorial = None

    @classmethod
    def registrar_editorial(cls, datos_editorial):
        cls.editorial = P_company(datos_editorial['nombre'])
        return cls.editorial

class ControladorLibro:

    book = None

    @classmethod
    def registrarLibro(cls, datos_libro):
        cls.book = Books(
            datos_libro['identifier'],
            datos_libro['p_company_id'],
            datos_libro['author_id'],
            datos_libro['book']
            )
        return cls.book