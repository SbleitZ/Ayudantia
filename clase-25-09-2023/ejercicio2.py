lista_contactos = []
'''
plantilla_diccionario = {
  "Nombre":"",
  "Teléfono":"",
  "Email":""
}
'''

estado_salida = False

def mostrar_contactos():
  i = 1
  for contacto in lista_contactos:
    nombre, telefono, email = contacto["Nombre"],contacto["Teléfono"],contacto["Email"]
    print(f"Contacto {i}")
    print(f"Nombre: {nombre}")
    print(f"Teléfono: {telefono}")
    print(f"Email: {email}")
    i+=1

while not estado_salida:
  print("1. Agregar contacto.")
  print("2. Eliminar contacto.")
  print("3. Mostrar contactos.")
  print("4. Salir.")
  opcion = int(input("Elige una opción, según el indice: "))
  if(opcion == 1):

    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el teléfono del contacto: ")
    email = input("Ingresa el email del contacto: ")
    plantilla_diccionario = {
      "Nombre":nombre,
      "Teléfono":telefono,
      "Email":email
    }
    lista_contactos.append(plantilla_diccionario)
    continue
  if(opcion == 2):
    mostrar_contactos()
    indice_contacto = int(input("Elige el contacto, según el indice: "))-1
    lista_contactos.pop(indice_contacto)
    continue
  if(opcion == 3):
    if len(lista_contactos) == 0:
      print("Tienes 0 contactos.")
    else:
      mostrar_contactos()
    continue
  if(opcion == 4):
    estado_salida = True
