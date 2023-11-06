import matplotlib.pyplot as plt
from tkinter import *
import random
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

def mostrar_grafico():
  plt.plot(x, y)
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.title('Gráfico de Líneas')
  plt.show()
def actualizar_grafico():
  x.clear()
  y.clear()
  for i in range(0,50):
    x.append(i)
    y.append(random.randint(0,50))
    max_v = max(y)
    min_v = min(y)
    maximo.config(text=f"Maximo : {max_v}")
    minimo.config(text=f"Maximo : {min_v}")
def grafico_rojo():
  plt.plot(x, y,color="red")
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.title('Gráfico de Líneas')
  plt.show()
ventana = Tk()

ventana.geometry("500x500")
ventana.title("Programa grafico")

# Datos para el eje x e y

# Mostrar el gráfico
btn = Button(ventana,text="Mostrar grafico", command=mostrar_grafico)
btn.pack()
btn_actualizar = Button(ventana,text="Actualizar grafico",command=actualizar_grafico)
btn_actualizar.pack()
btn_rojo = Button(ventana,text="Grafico Rojo",command=grafico_rojo)
btn_rojo.pack()
maximo = Label(ventana,text="Maximo: 0")
maximo.pack()
minimo = Label(ventana,text="Minimo: 0")
minimo.pack()
ventana.mainloop()