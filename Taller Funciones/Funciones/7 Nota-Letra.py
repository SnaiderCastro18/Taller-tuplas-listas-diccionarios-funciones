estudiantes = {
    "Snaider": 4.8,
    "Valentina": 3.5,
    "Camilo": 2.1,
    "Sofia": 4.2,
    "Mateo": 1.8
}

ESCALA = (
    (4.5, 5.0, "A"),
    (3.5, 4.4, "B"),
    (3.0, 3.4, "C"),
    (2.0, 2.9, "D"),
    (0.0, 1.9, "F")
)

def generar_reporte(datos_estudiantes, rangos):
    print("\nREPORTE DE NOTAS\n")
    
    for nombre, nota in datos_estudiantes.items():
    
        for minimo, maximo, letra in rangos:
            if minimo <= nota <= maximo:
                letra_final = letra
                break
        
        print(f"Estudiante: {nombre} | Nota: {nota} | Letra: {letra_final}\n")

generar_reporte(estudiantes, ESCALA)