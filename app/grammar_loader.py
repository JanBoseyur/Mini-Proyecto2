
def cargar_gramatica(ruta):
    
    gramatica = {}
    
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue

            izquierda, derecha = linea.split("::=")
            izquierda = izquierda.strip()
            producciones = derecha.split("|")

            gramatica[izquierda] = [
                [token.strip() for token in prod.split()]
                for prod in producciones
            ]

    return gramatica
