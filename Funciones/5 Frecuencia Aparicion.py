lista = [("Pablo"),("Maria"),("Juan"),("Ana"),("Pedro"),("Luis"),("Pablo"),("Maria"),("Juan"),("Ana"),("Luis"),("Pablo"),("Maria"),("Juan"),("Luis")]
def frecuencia_aparicion(lista):

    frecuencia = {}

    for elemento in lista:

        if elemento in frecuencia:

            frecuencia[elemento] += 1

        else:

            frecuencia[elemento] = 1

    return frecuencia
resultado = frecuencia_aparicion(lista)
print(resultado)
