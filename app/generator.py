
from derivator import derivar
from mutator import mutar

def generar_casos(gramatica, n=10, prof=10, longitud_max=50):
    casos = []

    for _ in range(n):

        # CASO VÁLIDO
        cadena = derivar(gramatica, "<expr>", profundidad_max=prof)
        casos.append({
            "cadena": cadena,
            "categoria": "valida",
            "longitud": len(cadena)
        })

        # CASO INVALIDO
        cadena_invalida = mutar(cadena)
        casos.append({
            "cadena": cadena_invalida,
            "categoria": "invalida",
            "longitud": len(cadena_invalida)
        })

        # CASO EXTREMO
        cadena_extrema = derivar(gramatica, "<expr>", profundidad_max=prof*2)
        if len(cadena_extrema) < longitud_max:
            cadena_extrema = cadena_extrema * 2  # volverla gigante

        casos.append({
            "cadena": cadena_extrema,
            "categoria": "extrema",
            "longitud": len(cadena_extrema)
        })

    return casos
