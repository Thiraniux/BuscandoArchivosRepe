import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

cantidaprint = int(print("Ingrese la cantidad de Carpetas a utilizar"))
                  
while conteo<=cantidaprint:
    ruta = filedialog.askdirectory(title ="Selecciona carpteta")
conteo= conteo+1
print("Ruta seleccionada:", ruta)