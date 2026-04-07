productos = {
    "leche": 7000,
    "pan": 2000,
    "arroz": 5000,
    "cafe": 5500
}

carrito = []

def obtener_catalogo():
    return productos

def sumar_al_carrito(nombre_producto):
    if nombre_producto in productos:
        carrito.append(nombre_producto)
        return True
    return False

def obtener_carrito():
    return carrito

def calcular_total():
    return sum(productos[item] for item in carrito)