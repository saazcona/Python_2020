from tkinter import *

ventana = Tk()

ventana.title("Grid System")

radio1 = Radiobutton(ventana, text = "SQL", value = 1)
radio2 = Radiobutton(ventana, text = "Python", value = 2)
radio3 = Radiobutton(ventana, text = "Java", value = 3)

radio1.grid(row = 0, column = 0)
radio2.grid(row = 0, column = 1)
radio3.grid(row = 0, column = 2)


ventana.geometry("250x100")
ventana.mainloop()