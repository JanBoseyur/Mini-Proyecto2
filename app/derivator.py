
import random

def derivar(gramatica, simbolo, profundidad_max=10, profundidad_actual=0):
    if profundidad_actual > profundidad_max:
        return ""

    # Si el símbolo es terminal (no aparece en la gramatica)
    if simbolo not in gramatica:
        return simbolo

    produccion = random.choice(gramatica[simbolo])
    resultado = ""

    for token in produccion:
        resultado += derivar(
            gramatica,
            token,
            profundidad_max,
            profundidad_actual + 1
        )

    return resultado
