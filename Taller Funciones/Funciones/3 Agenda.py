contactos = {}

def guardar():
    nombre = input("Nombre: ")
    contactos[nombre] = input("Teléfono: ")
    print(f"{nombre} guardado.")

def borrar():
    nombre = input("Nombre a borrar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"{nombre} eliminado.")
    else:
        print("No existe ese contacto.")

while True:
    print("\n AGENDA   1.Guardar  2.Ver  3.Borrar  4.Salir")
    opcion = input("Elige: ")

    if opcion == "1":
        guardar()
    elif opcion == "2":
        print("Tus contactos:", contactos)
    elif opcion == "3":
        borrar()
    elif opcion == "4":
        break
    else:
        print("Opción incorrecta.")