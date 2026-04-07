temperaturas ={
   "Bogota": [20, 21, 19, 22, 20, 18, 21],
   "Medellin": [25, 26, 24, 27, 25, 23, 26],
   "Cali": [30, 31, 29, 32, 30, 28, 31],
   "Barranquilla": [28, 29, 27, 30, 28, 26, 29]
}
def temperatura_maxima_semanal(temperaturas):
    maximas = {}
    for ciudad, temp in temperaturas.items():
        maximas[ciudad] = max(temp)
    return maximas

def temperatura_minima_semanal(temperaturas):
    minimas = {}
    for ciudad, temp in temperaturas.items():
        minimas[ciudad] = min(temp)
    return minimas
print("Temperaturas máximas semanales por ciudad:")
print(temperatura_maxima_semanal(temperaturas))
print("\nTemperaturas mínimas semanales por ciudad:")
print(temperatura_minima_semanal(temperaturas))

