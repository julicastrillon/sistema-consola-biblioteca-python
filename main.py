from clases.libro import Libro
from clases.prestamo import Prestamo
from clases.usuario import Usuario


def registrar_libro():
    titulo = input("\nTítulo: ")
    anio = input("Año: ")
    autor = input("Autor: ")

    libro = Libro(titulo, anio, autor)
    return libro


def registrar_usuario():
    nombre = input("\nNombre : ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")

    usuario = Usuario(nombre, direccion, telefono)
    return usuario


def registrar_prestamo(usuarios, libros):
    nombre_usuario = input("\nNombre del usuario: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("No existe el usuario registrado")
        return

    # Código copiado de digital house content

    titulo_libro = input("Título del libro: ")
    libro = next((l for l in libros if l.titulo == titulo_libro and l.disponible), None)
    if not libro:
        print("\nLibro no encontrado o no disponible.")
        return

    prestamo = Prestamo(usuario, libro)
    usuario.registrar_prestamo(prestamo)
    libro.disponible = False
    print("\nPréstamo registrado con éxito.")

    # Intento de código propio
    """libros_prestados = []

    while True:
        nombre_libro = input(
            "Titulo del libro a retirar (dejar vacío para finalizar): "
        )
        if not nombre_libro:
            break
        libro = next(
            (p for p in biblioteca.lista_de_libros if p.titulo == nombre_libro),
            None,
        )
        if libro:
            if libro.estado == "Retirado":
                print("El libro no se encuentra disponible")
            else:
                libros_prestados.append(libro)
        else:
            print("No se encuentra el titulo ingresado en nuestra biblioteca")

    if libros_prestados:
        prestamo = Prestamo(usuario, libros_prestados)
        prestamo.registrar_prestamo()
        print("El préstamo se ha registrado con éxito")
    else:
        print("No se ha podido registrar el préstamo")
    """


def registrar_devolucion(usuarios, libros):
    nombre_usuario = input("\nNombre del usuario: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("No existe el usuario registrado")
        return

    # Código copiado de digital house content

    titulo_libro = input("Título del libro: ")
    prestamo = next(
        (
            p
            for p in usuario.libros_prestados
            if p.libro.titulo == titulo_libro and not p.fecha_devolucion
        ),
        None,
    )
    if not prestamo:
        print("\nPréstamo no encontrado.")
        return

    prestamo.registrar_devolucion()
    print("\nDevolución registrada con éxito.")

    # Intento de código propio
    """
    libros_devueltos = []

    while True:
        nombre_libro = input(
            "Titulo del libro a devolver (dejar vacío para finalizar): "
        )
        if not nombre_libro:
            break
        libro = next(
            (d for d in biblioteca.lista_de_libros if d.titulo == nombre_libro), None
        )
        if libro:
            libros_devueltos.append(libro)
        else:
            print("No se encuentra el titulo ingresado en nuestra biblioteca")

    if libros_devueltos:
        devolucion = Devolucion(usuario, libros_devueltos)
        devolucion.registrar_devolucion()
        print("La devolución se ha registrado con éxito")
    else:
        print("No se ha podido registrar la devolución")
    """


def mostrar_menu():
    print("\n --- Menú de gestión de Biblioteca Popular ---")
    print("1. Registrar Libro")
    print("2. Registrar Usuario/Modificar Usuario existente")
    print("3. Registrar Préstamo")
    print("4. Registrar Devolución")
    print("5. Mostrar información acerca de Libros")
    print("6. Mostrar información acerca de Usuarios")
    print("7. Salir")


def main():
    usuarios = []
    libros = []

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n*REGISTRAR LIBRO*")
            libro = registrar_libro()
            if libro:
                libros.append(libro)
                print("\nLibro registrado exitosamente")

        elif opcion == "2":
            print("\n*REGISTRAR USUARIO*")
            usuario = registrar_usuario()
            if usuario:
                usuarios.append(usuario)
                print("\nUsuario registrado exitosamente")

        elif opcion == "3":
            print("\n*REGISTRAR PRÉSTAMO*")
            registrar_prestamo(usuarios, libros)

        elif opcion == "4":
            print("\n*REGISTRAR DEVOLUCIÓN*")
            registrar_devolucion(usuarios, libros)

        elif opcion == "5":
            print("\n*INFORMACIÓN DE LIBROS*")
            if libros == []:
                print("\nNo hay libros registrados")
            else: 
                for libro in libros:
                    print(libro.mostrar_informacion())

        elif opcion == "6":
            print("\n*INFORMACIÓN DE USUARIOS*")
            if usuarios == []:
                print("\nNo hay usuarios registrados")
            else: 
                for usuario in usuarios:
                    print(usuario.mostrar_informacion())
                    if usuario.libros_prestados == []:
                        print(f"El usuario {usuario.nombre} no tiene préstamos")
                    else:
                        for prestamo in usuario.libros_prestados:
                            print(prestamo.mostrar_informacion())   

        elif opcion == "7":
            print("\nSaliendo del sistema. Gracias por usar Biblioteca Popular APP!")
            break

        else:
            print("\nOpción no válida, intente nuevamente")


if __name__ == "__main__":
    main()
