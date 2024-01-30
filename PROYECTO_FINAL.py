#PROYECTO N°1 SISTEMA DE INVENTARIO PARA UNA FERRETERIA, REALIZADO POR: 
#Araque Rosbely C.I 27.513.037
#Ortegano Dabriela C.I 26.636.638

print("Bienvenido al Sistema de Administración de Inventario para una Ferretería")

# Estructura de datos para almacenar los productos
# Usamos un diccionario donde la clave es el nombre del producto y el valor es una tupla con la categoría, cantidad y precio
inventario = {}

# Variable para controlar el ciclo del menú
opcion = 0

# Ciclo del menú
while opcion != 6:
    # Mostramos las opciones disponibles 
    print("Seleccione una opción:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Mostrar inventario")
    print("6. Salir")

    # Pedimos al usuario que ingrese una opción
    opcion = int(input("Ingrese una opción: "))

    # Verificamos que la opción sea válida
    if opcion >= 1 and opcion <= 6:
        # Ejecutamos el código correspondiente a la opción elegida
        if opcion == 1:
            # Código para agregar un nuevo producto al inventario
            # Pedimos al usuario que ingrese los datos del producto
            nombre = input("Ingrese el nombre del producto: ").lower()
            categoria = input("Ingrese la categoría del producto: ").lower()
            cantidad = int(input("Ingrese la cantidad en stock del producto: "))
            precio = float(input("Ingrese el precio del producto: "))

            # Verificamos que el producto no exista previamente
            if nombre in inventario:
                print("El producto ya existe en el inventario.")
            else:
                # Agregamos el producto al inventario
                inventario[nombre] = (categoria, cantidad, precio)
                print("El producto se ha agregado al inventario.")
        elif opcion == 2:
            # Código para eliminar un producto existente del inventario
            # Pedimos al usuario que ingrese el nombre del producto a eliminar
            nombre = input("Ingrese el nombre del producto a eliminar: ").lower()

            # Verificamos que el producto exista en el inventario
            if nombre in inventario:
                # Eliminamos el producto del inventario
                del inventario[nombre]
                print("El producto se ha eliminado del inventario.")
            else:
                print("El producto no existe en el inventario.")

        elif opcion == 3:
            # Código para buscar un producto por nombre o categoría
            # Pedimos al usuario que elija el criterio de búsqueda
            criterio = input("Ingrese el criterio de búsqueda (nombre o categoria): ").lower()

            # Verificamos que el criterio sea válido
            if criterio == "nombre" or criterio == "categoria":
                # Pedimos al usuario que ingrese el valor a buscar
                valor = input("Ingrese los datos: ").lower()
                # Creamos una lista vacía para almacenar los productos encontrados
                productos_encontrados = []

                # Recorremos las claves del diccionario (los nombres de los productos)
                for nombre_producto in inventario:
                    # Obtenemos los datos del producto a partir de su nombre
                    datos_producto = inventario[nombre_producto]
                    # Obtenemos la categoría, cantidad y precio del producto
                    categoria, cantidad, precio = datos_producto

                    # Si el criterio es nombre, comparamos el nombre del producto con el valor
                    if criterio == "nombre" and nombre_producto == valor:
                        # Añadimos el producto a la lista de productos encontrados
                        productos_encontrados.append((nombre_producto, categoria, cantidad, precio))

                    # Si el criterio es categoría, comparamos la categoría del producto con el valor
                    elif criterio == "categoria" and categoria == valor:
                        # Añadimos el producto a la lista de productos encontrados
                        productos_encontrados.append((nombre_producto, categoria, cantidad, precio))

                # Verificamos si se encontraron productos
                if productos_encontrados:
                    # Mostramos los productos encontrados
                    print("Productos encontrados:")
                    for producto in productos_encontrados:
                        # Obtenemos el nombre, categoría, cantidad y precio del producto
                        nombre, categoria, cantidad, precio = producto

                        # Mostramos los datos del producto
                        print("Nombre:", nombre)
                        print("Categoria:", categoria)
                        print("Cantidad:", cantidad)
                        print("Precio: $", precio)
                        print("-----------------------")
                else:
                    # Mostramos un mensaje indicando que no se encontraron productos
                    print("No se encontraron productos con ese criterio y valor.")
            else:
                # Mostramos un mensaje indicando que el criterio no es válido
                print("El criterio no es válido. Debe ser nombre o categoría.")
            
        elif opcion == 4:
            # Código para actualizar la cantidad en stock y el precio de un producto existente
            # Pedimos al usuario que ingrese el nombre del producto a actualizar
            nombre = input("Ingrese el nombre del producto a actualizar: ").lower()

            # Verificamos que el producto exista en el inventario
            if nombre in inventario:
                # Obtenemos la categoría, cantidad y precio actuales del producto
                categoria, cantidad, precio = inventario[nombre]

                # Pedimos al usuario que ingrese la nueva cantidad y el nuevo precio del producto
                nueva_cantidad = int(input("Ingrese la nueva cantidad en stock del producto: "))
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                nueva_categoria = input ("Ingrese la nueva categoria:").lower()

                # Actualizamos el producto en el inventario
                inventario[nombre] = (nueva_categoria, nueva_cantidad, nuevo_precio)
                print("El producto se ha actualizado en el inventario.")
            else:
                print("El producto no existe en el inventario.")
        elif opcion == 5:
            # Código para mostrar el inventario actual
            # Verificamos si el inventario está vacío
            if inventario:
                # Mostramos el inventario
                print("Inventario actual:")
                for nombre in inventario:
                    # Obtenemos la categoría, cantidad y precio del producto
                    categoria, cantidad, precio = inventario[nombre]

                    # Mostramos los datos del producto
                    print("Nombre:", nombre)
                    print("Categoría:", categoria)
                    print("Cantidad:", cantidad)
                    print("Precio: $", precio)
                    print("-----------------------")
            else:
                # Mostramos un mensaje indicando que el inventario está vacío
                print("El inventario está vacío.")
        elif opcion == 6:
            # Código para salir del programa
            print("Gracias por usar el sistema. Hasta pronto.")
            break

        # Mostramos una línea en blanco para separarlas operaciones
        print()
    else:
        # Mostramos un mensaje indicando que la opción no es válida
        print("La opción no es válida. Debe ser un número entre 1 y 6.")

        # Mostramos una línea en blanco para separar las operaciones
        print()