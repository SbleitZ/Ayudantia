from tkinter import *
def calcular():
  resultado = eval(num.get())
  print(resultado)
ventana = Tk()
ventana.geometry("300x300")
ventana.title("Calculadora")
num = StringVar()
primer_label = Label(ventana,text="Primer numero: ")
primer_label.place(x=20,y=30)
primer_entry = Entry(ventana,textvariable=num)
primer_entry.place(x=140,y=30)
label_resultado = Label(ventana,text="El resultado es: ")
label_resultado.place(x=20,y=180)
btn = Button(text="Calcular",command=calcular)
btn.place(x=140,y=120)
ventana.mainloop()