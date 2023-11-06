from tkinter import *

def abrir_ventana(color):
    new_window = Toplevel(root)
    new_window.title("Ventana de Color")
    new_window.geometry("300x200")

    def cerrar_ventana():
        new_window.destroy()
        root.deiconify()

    new_window.configure(bg=color)

    return_button = Button(new_window, text="Volver a la ventana principal", command=cerrar_ventana)
    return_button.pack()

def ventana_amarilla():
    abrir_ventana("yellow")
    root.withdraw()
def ventana_azul():
    abrir_ventana("blue")
    root.withdraw()

def ventana_roja():
    abrir_ventana("red")
    root.withdraw()

root = Tk()
root.title("Selección de Color")
root.geometry("300x200")

yellow_button = Button(root, text="Amarillo", bg="yellow", command=ventana_amarilla)
yellow_button.pack()

blue_button = Button(root, text="Azul", bg="blue", command=ventana_azul)
blue_button.pack()

red_button = Button(root, text="Rojo", bg="red", command=ventana_roja)
red_button.pack()

root.mainloop()