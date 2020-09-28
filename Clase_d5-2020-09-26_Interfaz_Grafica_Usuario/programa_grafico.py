# Importar tkinter
from tkinter import *
# from tkinter.ttk import *


# Creamos un objeto del tipo Tk
ventana = Tk()

# Agregar un marco

marco1 = Frame(ventana, bg = "black")
marco1.pack(side = "top")

marco2 = Frame(ventana)
marco2.pack(side = "bottom")

# Agregar un Widget del tipo label

label1 = Label(marco1, text = 'Hola Mundo', font = ("Arial Bold", 20), fg = "blue")
label1.pack()

label2 = Label(marco2, text = 'Quiero azotar a María', font = ("Arial", 15), fg = "#545454")
label2.pack()

### Se agrega un botón
# Esto es un callback

nombre = StringVar()

textbox = Entry(ventana, textvariable = nombre)
textbox.pack()

labelnom = Label(ventana, text = "", textvariable = nombre)
labelnom.pack()

def boton_click(fulano):
    label1.configure(text = f"{fulano} Haz hecho Click en el puto botón")
    nombre.set(fulano)

boton = Button(ventana, text = "Bottom_text", bg = "red", fg = "white", command = lambda: boton_click("El Manin"))
boton.pack()
# Se establece el tamaño de la ventana

ventana.geometry("600x400") # Dimension de la ventana

# Se establece el mainloop para que la ventana queda abierta hasta que el usuario quiera
ventana.mainloop()

