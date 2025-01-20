"""
from datetime import datetime

class Devolucion:
    def __init__(self,usuario,libros_devueltos):
        self.usuario = usuario
        self.libros_devueltos = libros_devueltos
        self.fecha = datetime.now()

    def registrar_devolucion(self):
        self.usuario.registrar_devolucion(self)
        for libro in self.libros_devueltos:
                libro.devolver()
        libros = ", ".join([libro.titulo for libro in self.libros_devueltos])
        return f"{self.usuario.nombre} ha devuelto {libros}"
"""        