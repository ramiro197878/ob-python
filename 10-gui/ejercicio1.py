# En este ejercicio tenéis que crear una lista de RadioButton que muestre la
# opción que se ha seleccionado y que contenga un botón de reinicio para que
# deje todo como al principio.

# Al principio no tiene que haber una opción seleccionada.

import tkinter as tk

window = tk.Tk()

opcion = tk.IntVar()

tk.Radiobutton(window, text="Opcion 1", variable=opcion,
        value=1).pack()

tk.Radiobutton(window, text="Opcion 2", variable=opcion,
        value=2).pack()

tk.Radiobutton(window, text="Opcion 3", variable=opcion,
        value=3).pack()

def reset():
    opcion.set(None)

tk.Button(window, text="Reset", command=reset,).pack()

salida = tk.Label(window)
salida.pack()


window.mainloop()
