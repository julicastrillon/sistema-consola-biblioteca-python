class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.libros_prestados = []

    def actualizar_informacion(self, direccion=None, telefono=None):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono

    def registrar_prestamo(self,prestamo):
        self.libros_prestados.append(prestamo)
        

    def mostrar_informacion(self):
        return f"\nUsuario: {self.nombre}\nDirección: {self.direccion}\nTeléfono: {self.telefono}"
    
    
    # Intento de código propio
    """
    def mostrar_libros_prestados(self):
        if self.libros_prestados == []:
            return f"El usuario {self.nombre} no tiene libros retirados"
        else:
            return f"El usuario {self.nombre} tiene retirados {", ".join([libro.titulo for libro in self.libros_prestados])}"
    """