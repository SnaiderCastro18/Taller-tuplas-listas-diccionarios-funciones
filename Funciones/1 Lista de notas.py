notas_estudiantes = [50, 45, 16, 25, 30]

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def maxima(notas):
    return max(notas) 

def minima(notas):
    return min(notas) 

print(f"El promedio es: {calcular_promedio(notas_estudiantes)}")
print(f"La nota más alta es: {maxima(notas_estudiantes)}")
print(f"La nota más baja es: {minima(notas_estudiantes)}")