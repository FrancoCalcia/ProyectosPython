# Diccionario para almacenar el inventario
inventario = {}

# Función para agregar un producto al inventario
def agregarProducto():
    print("---------------------------")
    #Se le pide al usuario que ingrese los datos del producto
    codigo = input("Ingrese el código del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    marca = input("Ingrese la marca del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))
    precio = float(input("Ingrese el precio del producto: "))
    #Se guarda en el inventario el producto identificado por el codigo con sus respectivos datos
    inventario[codigo] = {"descripcion": descripcion, "marca": marca, "cantidad": cantidad, "precio": precio}
    print("Producto agregado al inventario.")
    print("---------------------------")

# Función para actualizar existencias de un producto
def actualizarExistencias():
    print("---------------------------")
    codigo = input("Ingrese el código del producto: ")
    if codigo in inventario:#Si el codigo esta en el inventario se procede a actualizar el stock
        nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
        inventario[codigo]["cantidad"] = nueva_cantidad
        print("Existencias actualizadas.")
    else:
        print("Producto no encontrado en el inventario.")
    print("---------------------------")

# Función para actualizar el precio de un producto
def actualizarPrecio():
    print("---------------------------")
    codigo = input("Ingrese el código del producto: ")
    if codigo in inventario:#Si el codigo esta en el inventario se procede a actualizar el precio
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        inventario[codigo]["precio"] = nuevo_precio
        print("Precio actualizado.")
    else:
        print("Producto no encontrado en el inventario.")
    print("---------------------------")

# Función para mostrar los productos del inventario
def Resumen():
    print("---------------------------")
    print("Inventario:")
    for codigo, producto in inventario.items():

        print(f"Código: {codigo}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Cantidad en stock: {producto['cantidad']}")
        print(f"Marca: {producto['marca']}")
        print(f"Precio: {producto['precio']}")
        print("---------------------------")


# Función principal donde se muestra el menú
def menu():
    while True:
        print("Menú:")
        print("a. Agregar producto")
        print("b. Actualizar existencia")
        print("c. Actualizar precio")
        print("d. Mostrar productos")
        print("e. Salir")

#se le indica al usuario que ingrese una opcion, en base a la ingresada se llama a las distintas funciones anteriormente programadas
        opcion = input("Elija una opción: ")

        if opcion == "a":
            agregarProducto()
        elif opcion == "b":
            actualizarExistencias()
        elif opcion == "c":
            actualizarPrecio()
        elif opcion == "d":
            Resumen()
        elif opcion == "e":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


menu() #llamado de la funcion main()