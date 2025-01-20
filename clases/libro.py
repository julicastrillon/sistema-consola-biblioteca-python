class Libro:
    def __init__(self, titulo, anio, autor):
        self.titulo = titulo
        self.anio = anio
        self.autor = autor
        self.disponible = True

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Retirado"
        return f"\nTítulo: {self.titulo}\nAño: {self.anio}\nAutor: {self.autor}\nEstado: {estado}"

    """
    def retirar(self):
        self.estado = "Retirado"
        return f"El libro {self.titulo} ha sido retirado"

    def devolver(self):
        self.estado = "Disponible"
        return f"El libro {self.titulo} ha sido devuelto"
    """