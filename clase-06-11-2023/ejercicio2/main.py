from tkinter import *
import random
from tkinter import messagebox
def generar_numeros_aleatorios():
  variable.set(str(random.randint(0,1000)))
  ventana.after(500,generar_numeros_aleatorios)


ventana = Tk()
ventana.geometry("300x300")
ventana.title("Generador de numeros aleatorios")
variable = StringVar()
messagebox.showinfo("Hola")
label = Label(ventana,textvariable=variable,background="#c2be76",padx=10,pady=10,height=3,width=3).pack()
btn = Button(ventana,text="Generar numeros aleatorios",command=generar_numeros_aleatorios).pack()
ventana.mainloop()