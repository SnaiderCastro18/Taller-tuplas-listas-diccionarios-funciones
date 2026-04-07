notas_estudiantes = [50, 45, 16, 25, 30]

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def obtener_maxima(notas):
    return max(notas) 

def obtener_minima(notas):
    return min(notas) 

print(f"El promedio es: {calcular_promedio(notas_estudiantes)}")
print(f"La nota más alta es: {obtener_maxima(notas_estudiantes)}")
print(f"La nota más baja es: {obtener_minima(notas_estudiantes)}")