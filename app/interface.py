
import tkinter as tk
from tkinter import filedialog, messagebox
from grammar_loader import cargar_gramatica
from generator import generar_casos
from metrics import calcular_metricas
import json
import os

def lanzar_interfaz():

    def cargar_archivo():
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de gramática",
            filetypes=[("Archivos TXT", "*.txt")]
        )
        entrada_gramatica.set(ruta)

    def ejecutar_generacion():
        ruta = entrada_gramatica.get()

        if not ruta:
            messagebox.showerror("Error", "Debe cargar un archivo de gramática")
            return

        try:
            gramatica = cargar_gramatica(ruta)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la gramática:\n{e}")
            return

        try:
            n = int(entrada_cantidad.get())
            prof = int(entrada_profundidad.get())
            long = int(entrada_longitud.get())
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar números válidos")
            return

        casos = generar_casos(gramatica, n, prof, long)
        metricas = calcular_metricas(casos)

        # Crear carpeta output si no existe
        if not os.path.exists("output"):
            os.makedirs("output")

        with open("output/resultados.json", "w", encoding="utf-8") as f:
            json.dump({"casos": casos, "metricas": metricas}, f, indent=4)

        # Mostrar métricas en la GUI
        texto_metricas = (
            f"Total: {metricas['total']}\n"
            f"Válidas: {metricas['validas']} ({metricas['porcentaje_validas']:.1f}%)\n"
            f"Inválidas: {metricas['invalidas']} ({metricas['porcentaje_invalidas']:.1f}%)\n"
            f"Extremas: {metricas['extremas']} ({metricas['porcentaje_extremas']:.1f}%)\n"
            f"Longitud promedio: {metricas['longitud_promedio']:.2f}\n"
            f"Longitud máxima: {metricas['longitud_max']}\n"
            f"Longitud mínima: {metricas['longitud_min']}\n"
        )
        texto_salida.delete("1.0", tk.END)
        texto_salida.insert(tk.END, texto_metricas)

        messagebox.showinfo("Éxito", "Casos generados y guardados en output/resultados.json")

    # ========= Construcción de la ventana =========
    root = tk.Tk()
    root.title("Generador Automático de Casos - INFO1148")
    root.geometry("500x600")

    # Variables de Tkinter
    entrada_gramatica = tk.StringVar()
    entrada_cantidad = tk.StringVar(value="5")
    entrada_profundidad = tk.StringVar(value="6")
    entrada_longitud = tk.StringVar(value="60")

    # Widgets GUI
    tk.Label(root, text="Generador Automático de Casos", font=("Arial", 15, "bold")).pack(pady=10)

    tk.Button(root, text="Cargar Gramática (.txt)", command=cargar_archivo, height=2).pack()
    tk.Entry(root, textvariable=entrada_gramatica, width=50).pack(pady=5)

    tk.Label(root, text="Cantidad de casos:").pack()
    tk.Entry(root, textvariable=entrada_cantidad).pack()

    tk.Label(root, text="Profundidad máxima:").pack()
    tk.Entry(root, textvariable=entrada_profundidad).pack()

    tk.Label(root, text="Longitud máxima:").pack()
    tk.Entry(root, textvariable=entrada_longitud).pack()

    tk.Button(root, text="Generar Casos", command=ejecutar_generacion, bg="lightgreen", height=2).pack(pady=10)

    tk.Label(root, text="Métricas del proceso:").pack()

    texto_salida = tk.Text(root, height=15, width=55)
    texto_salida.pack()

    root.mainloop()

