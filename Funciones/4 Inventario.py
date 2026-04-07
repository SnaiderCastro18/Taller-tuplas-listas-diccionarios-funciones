inventario = {"manzana": {"precio": 2500, "cantidad": 10}, "pera": {"precio": 3000, "cantidad": 5}, "naranja": {"precio": 2000, "cantidad": 8}, "mandarina": {"precio": 3500, "cantidad": 12}}

def calcular_inventario(inventario):
    total = 0
    for producto, datos in inventario.items():
        precio = datos["precio"]
        cantidad = datos["cantidad"]
        total += precio * cantidad
    return total

total_inventario = calcular_inventario(inventario)
print("\nEl valor total del inventario es:", total_inventario,"\n")
