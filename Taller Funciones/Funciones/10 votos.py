candidatos_oficiales = ("Ana", "Juan", "Luis")

votos_urna = ["Ana", "Juan", "Pedro", "Ana", "Luis", "Ana", "Carlos", "Juan"]

def votos(voto, candidatos):

    conteo = {"Nulos_Invalido": 0}
    for votos in candidatos:
        conteo[votos] = 0  
        
    for voto in voto:
        if voto in candidatos:
            conteo[voto] += 1
        else:
            conteo["Nulos_Invalido"] += 1
            
    return conteo


resultados = votos(votos_urna, candidatos_oficiales)
print(f"Resultados: {resultados}")
