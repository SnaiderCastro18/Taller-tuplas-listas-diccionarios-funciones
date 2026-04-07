from funcion import obtener_catalogo, sumar_al_carrito, obtener_carrito, calcular_total

while True:
        print("\n--- BIENVENIDO AL SUPERMERCADO ---")
        print("1. Ver productos y precios")
        print("2. Agregar producto al carrito")
        print("3. Ver mi carrito y total")
        print("4. Salir")
       
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            print("\nLISTA DE PRECIOS:")
            for p, precio in obtener_catalogo().items():
                print(f"-> {p.capitalize()}: ${precio}")

        elif opcion == "2":
            prod = input("Escribe el nombre del producto: ").lower()
            if sumar_al_carrito(prod):
                print(f"¡{prod} agregado con éxito!")
            else:
                print("Error: Producto no encontrado.")

        elif opcion == "3":
            print(f"\nTu carrito actual: {obtener_carrito()}")
            print(f"TOTAL A PAGAR: ${calcular_total():.2f}")

        elif opcion == "4":
            print("Gracias por visitarnos. ¡Adiós!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
