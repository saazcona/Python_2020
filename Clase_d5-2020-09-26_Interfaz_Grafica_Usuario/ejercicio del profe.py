from tkinter import *
from tkinter.ttk import *

root = Tk()

dolar = StringVar()

txtdolar = Entry(root, textvariable = dolar)
txtdolar.pack()

resultado = StringVar()

lblResultado = Label(root, text = '',font = ("Arial", 25), textvariable = resultado)
lblResultado.pack()

combo = Combobox(root)
combo['values'] = ("Lunes", "Martes", "Miercoles")
combo.pack(pady = 15)

lista = Listbox(root)
lista.insert(0, "María")
lista.insert(1, "Pirulo")
lista.insert(2, "Jonas")
lista.insert(3, "Agripino")
lista.pack()

radio1 = Radiobutton(root, text = "SQL", value = 1)
radio2 = Radiobutton(root, text = "Python", value = 2)
radio3 = Radiobutton(root, text = "Java", value = 3)
radio1.pack()
radio2.pack()
radio3.pack()

def convertir_dolar():
    resultado.set(str(float(dolar.get()) * 58.5))

boton_calcular = Button(root, text = "Convertir", command=convertir_dolar)
boton_calcular.pack()

# Se establece el tamaño de la root

root.geometry("600x400") # Dimension de la root

# Se establece el mainloop para que la root queda abierta hasta que el usuario quiera
root.mainloop()