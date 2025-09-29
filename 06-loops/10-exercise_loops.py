# Crearás un carrito de compras que haga las siguientes funcionalidades:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

option = ''
shopping_cart = ["Laptop", "Vaso", "Cafe", "Audifonos"]

while option != '7':
    print()
    print('******************************')
    print("Opciones: ")
    print("Carrito de compras")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar la lista ordenada")
    print("4. Buscar producto")
    print("5. Contar productos del carrito")
    print("6. Vaciar el carrito")
    print("7. Salir")
    print('******************************')

    option = input("Elige una opción (1-7): ")

    if option == "1":
        print('Carrito actual: ', shopping_cart)
        product = input('Que producto deseas agregar?: ')
        shopping_cart.append(product)
        print('Producto agregado: ',product)
        print('Carrito actualizado: ', shopping_cart)
    elif option == "2":
        print('Carrito actual: ', shopping_cart)
        product = input("Ingresa un nombre de producto: ")
        if product in shopping_cart:
            shopping_cart.remove(product)
            print("Producto eliminado")
            print('Carrito actualizado: ', shopping_cart)
        else:
            print("El producto no está en la lista")
    
    elif option == "3":
        print('Carrito actual: ', shopping_cart)
        new_shopping_cart = sorted(shopping_cart)
        print('Carrito Ordenado: ', new_shopping_cart)
    elif option == "4":
        product = input('Ingresa el nombre de producto a buscar: ')
        if product in shopping_cart:
            print(f'{product} esta en la lista de compras')
        else:
            print('Producto no encontrado')
    elif option == "5":
        print('Total de productos: ', len(shopping_cart))
    elif option == "6":
        shopping_cart.clear()
        print('Carrito vacio', shopping_cart)
    else:
        print('Opción no válida')
else:
    print('Hasta luego')
