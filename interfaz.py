import tkinter as tk
from airport import *
# tu código de aeropuertos ya definido
import matplotlib.pyplot as plt

# --- Ventana principal ---
root = tk.Tk()
root.geometry("1280x720")

# --- Matriz principal ---
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# --- Primer cuadradito, seguramente plots ---
button_picture_frame = tk.LabelFrame(root, text="lo que sea")
button_picture_frame.grid(row=0, column=0, padx=0, pady=0, sticky=tk.N+tk.E+tk.S+tk.W)
button_picture_frame.rowconfigure(0, weight=1)
button_picture_frame.rowconfigure(1, weight=1)
button_picture_frame.columnconfigure(0, weight=1)

button1 = tk.Button(button_picture_frame, text="Mostrar shengens", command=lambda: None)  # placeholder
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(button_picture_frame, text="dejar de mostrar shengens", command=lambda: None)  # placeholder
button2.grid(row=1, column=0, padx=5, pady=5)

# --- Segundo cuadradito para los plots ---
button_graph_frame = tk.LabelFrame(root, text="Grafics")
button_graph_frame.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N+tk.E+tk.S+tk.W)
button_graph_frame.rowconfigure(0, weight=1)
button_graph_frame.rowconfigure(1, weight=1)
button_graph_frame.columnconfigure(0, weight=1)

# Funciones para los botones de los plots
def ppp():  # plot 1 → proporción Schengen
    PlotSchengenRatio(airports)

def plot2():  # plot 2 → mapa de aeropuertos
    PlotAirports(airports)

button3 = tk.Button(button_graph_frame, text="enseñar plot 1", command=ppp)
button3.grid(row=0, column=0, padx=5, pady=5)

button4 = tk.Button(button_graph_frame, text="enseñar plot 2", command=plot2)
button4.grid(row=1, column=0, padx=5, pady=5)

# --- Tercer cuadradito, seguramente añadir y eliminar aeropuertos ---
input_frame = tk.LabelFrame(root, text="Buscar aeropuerto")
input_frame.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N+tk.E+tk.S+tk.W)
input_frame.rowconfigure(0, weight=1)
input_frame.rowconfigure(1, weight=1)
input_frame.columnconfigure(0, weight=1)

entry = tk.Entry(input_frame)
entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.E+tk.S)

button5 = tk.Button(input_frame, text="Buscar aeropuerto", command=lambda: None)  # placeholder
button5.grid(row=1, column=0, padx=5, pady=5)

# --- Columna derecha: Mapa ---
picture_frame = tk.LabelFrame(root, text="Mapa")
picture_frame.grid(row=0, column=1, rowspan=3, padx=5, pady=5, sticky="nsew")
picture_frame.rowconfigure(0, weight=1)
picture_frame.columnconfigure(0, weight=1)

# --- Ejecutar interfaz ---
root.mainloop()