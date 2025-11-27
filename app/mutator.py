
import random

def eliminar_parentesis(expr):
    return expr.replace("(", "", 1) if "(" in expr else expr + "("

def reemplazar_operador(expr):
    operadores_invalidos = ["$", "&", "?", "@", "!"]
    pos = random.randint(0, len(expr)-1)
    return expr[:pos] + random.choice(operadores_invalidos) + expr[pos+1:]

def insertar_simbolo_raro(expr):
    raros = ["#", "~", "^", "|"]
    pos = random.randint(0, len(expr))
    return expr[:pos] + random.choice(raros) + expr[pos:]

def cortar_expr(expr):
    if len(expr) < 3:
        return expr
    return expr[:len(expr)//2]

def mutar(expr):
    mutadores = [
        eliminar_parentesis,
        reemplazar_operador,
        insertar_simbolo_raro,
        cortar_expr
    ]
    return random.choice(mutadores)(expr)
