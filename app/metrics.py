
def calcular_metricas(casos):
    total = len(casos)
    validas = sum(1 for c in casos if c["categoria"] == "valida")
    invalidas = sum(1 for c in casos if c["categoria"] == "invalida")
    extremas = sum(1 for c in casos if c["categoria"] == "extrema")

    longitudes = [c["longitud"] for c in casos]

    return {
        "total": total,
        "validas": validas,
        "invalidas": invalidas,
        "extremas": extremas,
        "porcentaje_validas": validas / total * 100,
        "porcentaje_invalidas": invalidas / total * 100,
        "porcentaje_extremas": extremas / total * 100,
        "longitud_promedio": sum(longitudes) / total,
        "longitud_max": max(longitudes),
        "longitud_min": min(longitudes)
    }
