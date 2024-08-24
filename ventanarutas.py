import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

ruta = filedialog.askdirectory(title ="Selecciona carpteta")

print("Ruta seleccionada:", ruta)