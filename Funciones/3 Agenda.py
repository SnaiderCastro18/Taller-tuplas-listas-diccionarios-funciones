agenda = {}

def agregar_contacto():
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el teléfono: ")
    agenda[nombre] = telefono
    print(f"\n{nombre} ha sido guardado.")

def eliminar_contacto():
    nombre = input("Ingresa el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"\n{nombre} ha sido eliminado.")
    else:
        print(f"\n{nombre} no se encuentra en la agenda.")

while True:
    print("\n AGENDA ")
    print("1. Agregar contacto")
    print("2. Ver todos")
    print("3. Eliminar contacto")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        print("\nLista de contactos:", agenda)
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        print("\nSaliendo\n")
        break 
    else:
        print("\nOpción no válida, intenta de nuevo.")



    
        