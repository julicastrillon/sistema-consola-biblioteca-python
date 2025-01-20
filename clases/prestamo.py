from datetime import datetime


class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_retirada = datetime.now()
        self.fecha_devolucion = None

    def registrar_devolucion(self):
        self.fecha_devolucion = datetime.now()
        self.libro.disponible = True

    def mostrar_informacion(self):
        fecha_devolucion = (
            self.fecha_devolucion if self.fecha_devolucion else "No devuelto"
        )
        print(f"\n *PRÉSTAMOS DE USUARIO {self.usuario.nombre}*")
        return f"\nLibro: {self.libro.titulo}\nFecha de Préstamo: {self.fecha_retirada}\nFecha de Devolución: {fecha_devolucion}"

    """
    def registrar_prestamo(self):
        self.usuario.registrar_prestamo(self)
        for libro in self.libros_prestados:
            libro.retirar()
        libros = ", ".join([libro.titulo for libro in self.libros_prestados])
        print(f"{self.usuario.nombre} ha retirado {libros}")
    """
