productos = [("Manzana", "Fruta"),
            ("Lechuga", "Verdura"),
            ("Zanahoria", "Verdura"),
            ("leche", "Lácteo"),
            ("Yogurt", "Lácteo"),
            ("Mandarina", "Fruta")]

def agrupar_productos_por_categoria(productos):

    categorias = {}

    for producto, categoria in productos:

        if categoria not in categorias:

            categorias[categoria] = []

        categorias[categoria].append(producto)

    return categorias

print("\nProductos agrupados por categoría:")

print(agrupar_productos_por_categoria(productos))



              
