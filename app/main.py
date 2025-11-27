
import json
from grammar_loader import cargar_gramatica
from generator import generar_casos
from metrics import calcular_metricas

from interface import lanzar_interfaz

def main():
    gramatica = cargar_gramatica("gramatica.txt")

    casos = generar_casos(gramatica, n=5, prof=6, longitud_max=60)

    metricas = calcular_metricas(casos)

    # Guardar en JSON
    with open("output/resultados.json", "w", encoding="utf-8") as f:
        json.dump({
            "casos": casos,
            "metricas": metricas
        }, f, indent=4)

    print("Generación completa. Ver output/resultados.json")

if __name__ == "__main__":
    lanzar_interfaz()

