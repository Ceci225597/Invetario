Inventario = {
    'cinturones': {'cantidad': 20, 'precio': 22.50},
    'sombreros': {'cantidad': 30, 'precio': 35.00},
    'tacones': {'cantidad': 60, 'precio': 205.63},
    'zapatos': {'cantidad': 42, 'precio': 300.50} 
}

#Añadir Producto#

nombre_producto = input ("ingrese el nombre del producto: ").strip ().capitalize()
if nombre_producto in Inventario :  
    print (f"Error: el producto '{nombre_producto}'ya existe en el inventario.")
else:
    print(f"Nombre '{nombre_producto}' disponible.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad inicial: "))
        if cantidad < 0 :
            print ("La cantidad no puede ser negativa. Intente de nuevo.")
        else :
            break 
    except ValueError:
        print ("Entrada invalida. Por favor, ingrese un numero entero para la cantidad.")

while True: 
    try: 
        precio = float (input("Ingrese el precio unitario : "))
        if precio < 0 :
            print("El precio no puede ser negativo. Intente de nuevo.")
        else :
            break
    except ValueError:
            print ("Entrada invalida. Por favor, ingrese un numero para el precio")

Inventario [nombre_producto] = {'cantidad': cantidad, 'precio' : precio}
print (f"Producto '{nombre_producto}' añadido exitosamente.")

##Actualizar Stock de producto 
nombre_a_actualizar = input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
if nombre_a_actualizar not in Inventario :
    print(f"Error: el producto '{nombre_a_actualizar}' no se encuentra en el inventario.")
else: 
    print(f"Producto '{nombre_a_actualizar}' encontrado. Cantidad actual: {Inventario[nombre_a_actualizar]['cantidad']}.")

while True:
    try:
        nueva_cantidad = int(input(f"Ingrese la nueva cantidad para '{nombre_a_actualizar}': "))
        if nueva_cantidad < 0 :
            print("La cantidad no puede ser negativa. Intente de nuevo.")
        else: 
            break
    except ValueError:
        print("Entrada invalida. Por favor, ingrese un numero entero para la cantidad.")

Inventario [nombre_a_actualizar]['cantidad'] = nueva_cantidad
print(f"Stock de '{nombre_a_actualizar}'actualizado a {nueva_cantidad}.")

##Eliminar Producto 
nombre_a_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
if nombre_a_eliminar not in Inventario:
    print(f"Error: El producto '{nombre_a_eliminar}'no se encuentra en el inventario.")
else:
    print(f"Producto '{nombre_a_eliminar}'encontrado.")
confirmacion= input(f"esta seguro de que desea eliminar '{nombre_a_eliminar}' del inventario? (si/no): ").lower()
if confirmacion == 'si':
    pass
else: 
    print("eliminacion cancelada.")
del Inventario [nombre_a_eliminar]
print (f"Producto '{nombre_a_eliminar}' eliminado exitosamente.")

##Ver inventario
if not Inventario:
    print("el inventario esta vacio")
else:
    print("\n---Inventario actual---")
    for nombre, detalles in Inventario.items():
        print(f"nombre: {nombre}, cantidad: {detalles ['cantidad']}, precio: ${detalles['precio']: .2f}")
        print("--------\n")

##Buscar producto 
termino_busqueda = input("Ingrese el nombre o parte del nombre del producto a buscar: ").strip().lower()
productos_encontrados = []
for nombre, detalles in Inventario. items():
    if termino_busqueda in nombre.lower():
        productos_encontrados.append ((nombre, detalles))

if productos_encontrados:
    print("\n---Resultados de la busqueda---")
    for nombre, detalles in productos_encontrados:
        print(f"nombre: {nombre}, cantidad: {detalles ['cantidad']}, precio: ${detalles['precio']:.2f}")
        print("-------\n")
    else: 
        print(f"no se encontraron productos que coincidan con '{termino_busqueda}'.")

##Resumen de inventario
valor_total_inventario = 0
for detalles in Inventario.values():
    valor_total_inventario += detalles ['cantidad']*detalles ['precio']
    print(f"valor total del inventario: ${valor_total_inventario : .2f}")
            
umbral_bajo_stock= 10
productos_bajo_stock=[]
for nombre, detalles in Inventario.items():
    if detalles ['cantidad'] < umbral_bajo_stock:
        productos_bajo_stock.apprend (nombre)

if productos_bajo_stock:
    print("Productos con bajo stock (cantidad < {}):".format (umbral_bajo_stock))
    for p in productos_bajo_stock: 
        print(f"-{p} (Cantidad: {Inventario[p]['cantidad']})")
    else:
        print("no hay productos con bajo stock.")

algun_producto_agotado = any (detalles['cantidad']==0 for detalles in Inventario.values())
if algun_producto_agotado:
    print("Advertencia!! Hay al menos un producto agotado en el inventario.")
else:
    print("no hay productos agotados en el inventario (o el inventario esta vacio).")

todos_con_stock_aceptable= all(detalles['cantidad']>0 for detalles in Inventario.values())
if Inventario and todos_con_stock_aceptable:
    print("todos los productos en el inventario tienen stock aceptable")
elif Inventario:
    print("algunos productos tienen stock cero o negativo.")
else:
    print ("el inventario esta vacio, por lo que no hay productos con stock aceptable")

##Salir
print("saliendo del programa. Hasta pronto!!")

##ESTRUCTURA DE DATOS
Inventario = {
    'cinturones': {'cantidad': 20, 'precio': 22.50},
    'sombreros': {'cantidad': 30, 'precio': 35.00},
    'tacones': {'cantidad': 60, 'precio': 205.63},
    'zapatos': {'cantidad': 42, 'precio': 300.50} 
}
while True:
    print("\n---Menu de gestion de inventario---")
    print("1. Añadir producto")
    print("2. Actualizar stock")
    print("3. Eliminar producto")
    print("4. Ver inventario")
    print("5. Buscar producto")
    print("6. Resumen de inventario")
    print("------------")
    
    opcion= input("seleccione una opcion: ")
    if opcion == '1':
        print("\n---Añadir nuevo producto---")
        nombre_producto=input("ingrese el nombre del producto: ").strip().capitalize()
        if nombre_producto in Inventario :
            print(f"Error: el producto '{nombre_producto}' ya existe en el inventario.")
        else:
            while True:
                try:
                    cantidad = int (input("ingrese la cantidad inicial: "))
                    if cantidad < 0:
                        print("la cantidad no puede ser negativa. Intente de nuevo")
                    else:
                        break
                except ValueError:
                    print("entrada invalida. Por favor, ingrese un numero entero para la cantidad.")
                    while True:
                        try: 
                            precio = float(input("Ingrese el precio unitario: "))
                            if precio < 0:
                                print("El precio no puede ser negativo. Intente de nuevo.")
                            else:
                                break
                        except ValueError:
                            print("Entrada invalida. Por favor, ingrese un numero para el precio.")
                    Inventario[nombre_producto]= {'cantidad': cantidad, 'precio': precio}
                    print(f"Producto '{nombre_producto}' añadido exitosamente.")
                    
    elif opcion == '2':
        print("\n---Actualizar stock de producto---")
        nombre_a_actualizar= input("Ingrese el nombre del producto a actualizar: ").strip().capitalize()
        if nombre_a_actualizar not in Inventario:
            print(f"error: el producto '{nombre_a_actualizar}' no se encuentra en el inventario.")
        else:
            print(f"Producto '{nombre_a_actualizar}' encontrado. Cantidad actual: {Inventario [nombre_a_actualizar]['cantidad']}.")
            while True:
                try:
                    nueva_cantidad= int(input(f"Ingrese la nueva cantidad para '{nombre_a_actualizar}': "))
                    if nueva_cantidad < 0:
                        print("la cantidad no puede ser negativa. Inetnte de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero entero para la cantidad.")
                    Inventario[nombre_a_actualizar]['cantidad']=nueva_cantidad
                    print(f"Stock de '{nombre_a_actualizar}'actualizado a {nueva_cantidad}.")
    elif opcion == '3':
        print("\n---Eliminar Producto---")
        nombre_a_eliminar= input("ingrese el nombre del producto a eliminar: ").strip().capitalize()
        if nombre_a_eliminar not in Inventario:
            print(f"Error: el producto '{nombre_a_eliminar}' no se encuentra en el inventario.")
        else: 
            confirmacion=input(f"Esta seguro de que desea eliminar '{nombre_a_eliminar}' del inventario? (si/no): ").lower()
            if confirmacion == 'si':
                del Inventario [nombre_a_eliminar]
                print(f"Producto '{nombre_a_eliminar}' eliminado exitosamente. ")
            else:
                print("Eliminacion cancelada")
                
    elif opcion == '4':
        print("\n---Ver inventario---")
        if not Inventario:
            print("El inventario esta vacio")
        else:
            for nombre, detalles in Inventario.items():
                print(f"Nombre: {nombre}, cantidad: {detalles['cantidad']}, precio: ${detalles['precio']: .2f}")
    elif opcion == '5':
        print("\n---Buscar producto---")
        termino_busqueda=input("Ingrese el nombre o parte del nombre del producto a buscar: ").strip().lower()
        productos_encontrados=[]
        for nombre, detalles in Inventario.items():
            if termino_busqueda in nombre.lower():
                productos_encontrados.append((nombre, detalles))
                if productos_encontrados:
                    print("\n---Resultados de la busqueda---")
                    for nombre, detalles in productos_encontrados:
                        print(f"Nombre:{nombre}, cantidad:{detalles['cantidad']}, precio: ${detalles['precio']: .2f}")
                    else:
                        print(f"No se encontraron productos que coincidan con '{termino_busqueda}'.")

    elif opcion =='6':
        print("\n---Resumen de inventario---")
        valor_total_inventario= 0 
        for detalles in Inventario.values():
            valor_total_inventario += detalles ['cantidad'] * detalles['precio']
            print(f"valor total del inventario: ${valor_total_inventario: .2f}")

            umbral_bajo_stock= 10
            productos_bajo_stock=[]
            for nombre, detalles in Inventario.items():
                if detalles['cantidad']<umbral_bajo_stock:
                    productos_bajo_stock.append (nombre)
                    if productos_bajo_stock: 
                        print("Productos con bajo stock (cantidad < {}):". format(umbral_bajo_stock))
                        for p in productos_bajo_stock:
                            print(f"-{p} (Cantidad: {inventario[p]['cantidad']})")
                        else:
                            print("No hay productos con bajo stock.")

                            algun_producto_agotado= any(detalles['cantidad'] == 0 for detalles in Inventario.values())
                            if algun_producto_agotado:
                                print("Advertencia! hay al menos un producto agotado en el inventario.")
                            else: 
                                print("No hay productos agotados en el inventario")
                            
    elif opcion == '7':
        print("saliendo del programa. Hasta pronto!!!")
        break
    else: 
        print("Opcion invalida. Por favor, intente de nuevo.")