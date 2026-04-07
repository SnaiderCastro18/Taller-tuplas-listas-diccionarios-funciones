carrito = []

precios = {"manzana": 3500,"pan": 2000,"leche": 1500,"huevos": 4000,"pera": 2500}

def agregar_producto(lista_carrito,producto):
    lista_carrito.append(producto)
    print (f"\nse ha agregado {producto} al carrito.\n")

def calcular_todo(lista_carrito,precios):
    total = 0
    for productos in lista_carrito:
        precio = precios[productos]
        total = total + precio
    return total

def aplicar_descuento_porcentaje(total, porcentaje):
    descuento1 = porcentaje / 100
    cantidad_a_descontar = total * descuento1
    return total - cantidad_a_descontar

agregar_producto(carrito, "manzana")
agregar_producto(carrito, "leche")

subtotal = calcular_todo(carrito, precios)
print(f"\nSubtotal: ${subtotal}\n")

total_final = aplicar_descuento_porcentaje(subtotal, 7)
print(f"\nTotal a pagar con descuento es de ${total_final}\n")