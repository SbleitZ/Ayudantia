
archivo = open("usuarios.txt", "r")

intentos = 0
def verificar_usuario(usuario,password):
  for user in archivo.readlines():
    usuario_txt,password_txt = user.split(",")
    if usuario_txt == usuario and password_txt.strip() == password:
      return True
  return False
while intentos < 3:
  usuario = input("Ingresa tu usuario: ")
  password = input("Ingresa tu contraseña: ")
  if verificar_usuario(usuario,password):
    print(f"Bienvenido {usuario}")
    break
  else:
    print("Usuario incorrecto.")
    intentos +=1

if intentos > 3:
  print("Has superado los 3 intentos.")
