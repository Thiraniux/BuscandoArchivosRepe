import tkinter as tk
from tkinter import messagebox, ttk
import ProbandoPycharm as pb
from ProbandoPycharm import buscandoraiz, archivosdir


def obtener_seleccion():
    # Esto es una tupla con los índices (= las posiciones)
    # de los ítems seleccionados por el usuario.
    indices = listbox.curselection()
    print(indices)
    messagebox.showinfo(
        title="Ítems seleccionados",
        # Obtener el texto de cada ítem seleccionado
        # y mostrarlos separados por comas.
        message=", ".join(listbox.get(i) for i in indices)
    )

    buscandoraiz(listbox.get(i) for i in indices)

items = archivosdir()
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Lista en Tk")
listbox = tk.Listbox(ventana, selectmode=tk.EXTENDED)

if items:
    listbox.insert(tk.END, *items)
else:
    print("La lista 'items' está vacía o no se ha importado correctamente.")


#listbox.insert(0, *items)
listbox.pack()
boton_obtener_seleccion = ttk.Button(
    ventana,
    text="Obtener selección",
    command=obtener_seleccion
)
boton_obtener_seleccion.pack()
ventana.mainloop()
