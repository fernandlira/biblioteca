from models.modelos import (
    Author, P_company
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