# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual
# debe de contener una lista de elementos seleccionables, también debe de tener
# un label con el texto que queráis.

import tkinter as tk


window = tk.Tk()
window.geometry('300x200')
window.title("Lista de paises")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

tk.Label(window, text="Lista de paises").grid(row=0, column=0)

paises = ('Alemania', 'España', 'Italia', 'Francia', 'Portugal')

paises_lista = tk.StringVar(value=paises)


listbox = tk.Listbox(
        window,
        listvariable=paises_lista,
        height=6,
        selectmode='extended')

listbox.grid(
    column=0,
    row=1,
    sticky='nwes'
)


window.mainloop()
