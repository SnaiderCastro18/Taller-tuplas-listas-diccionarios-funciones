lista=[("Carlos",30),("Maria",25),("Juan",28),("Ana",50),("Cristian",40),("Luis",35)]

def nombre_aprobados(lista):

    aprobados = []

    for nombre, nota in lista:

        if nota >= 30:

            aprobados.append(nombre)

    return aprobados    

resultado = nombre_aprobados(lista)
print(resultado)