from tkinter import *

root = Tk()
root.title("Mostrar Imagen con Tkinter")

image_path = "img.png"  # Ruta de tu imagen
img = PhotoImage(file=image_path)

label = Label(root, image=img)
label.pack()

texto = Label(root,text="TEXTO EN LA IMAGEN").place(x=120,y=80)
root.mainloop()
