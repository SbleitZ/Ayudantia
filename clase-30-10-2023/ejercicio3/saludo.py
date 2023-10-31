from tkinter import *
from tkinter import messagebox
def saludo_personalizado():
  print("Hola, "+ nombre.get())
  messagebox.showinfo("Saludo personalizado","Hola, "+nombre.get())

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Saludo personalizado")
nombre = StringVar()
nombre_entry = Entry(ventana, textvariable=nombre)
nombre_entry.pack()
btn = Button(ventana,text="Mostrar saludo personalizado",command=saludo_personalizado).pack()
ventana.mainloop()