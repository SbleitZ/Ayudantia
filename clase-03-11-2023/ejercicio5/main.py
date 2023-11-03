from tkinter import *
from tkinter import messagebox
us = "Sbleit"
pw = "1234"
intentos = 0
def sesion_usuario():
  ventana.withdraw()
  sesion = Toplevel()
  sesion.geometry("300x300")
  sesion.title("Ventana de usuario")
  label = Label(sesion,text="Bienvenido").pack()
  def cerrar_sesion():
    sesion.destroy(),ventana.deiconify()
  volver = Button(sesion,text="Volver",command=cerrar_sesion).pack()
def verificar_sesion():
  global intentos
  intentos +=1
  if(intentos > 3):
    messagebox.showerror("Error","Alcanzaste tus intentos permitidos.")
    ventana.quit()
    return
  if usuario.get() == us and password.get() == pw:
    messagebox.showinfo("Verificación","Sesión exitosa.")
    sesion_usuario()
    return
  messagebox.showwarning("Verificación","Sesión fallida.")

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Inicio de sesión")
usuario = StringVar()
password = StringVar()
primer_label = Label(ventana,text="Usuario : ")
primer_label.place(x=20,y=30)
primer_entry = Entry(ventana,textvariable=usuario)
primer_entry.place(x=130,y=30)
segundo_label = Label(ventana,text="Contraseña : ")
segundo_label.place(x=20,y=80)
segundo_entry = Entry(ventana,textvariable=password,show="*")
segundo_entry.place(x=130,y=80)
btn = Button(text="Ingresar",command=verificar_sesion)
btn.place(x=130,y=120)
ventana.mainloop()