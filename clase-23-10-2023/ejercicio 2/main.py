'''
- Crear el entorno
- crear las clases solicitadas y sus respectivos constructores y atributos
- crear las funciones necesarias para cumplir con la instruccion principal
'''
from entidades.Tecnico import Tecnico
from entidades.Gerente import Gerente
e1 = Gerente("Teodoro Ribera","001-1",500000,2019)
e2 = Gerente("Sebastián Castillo","002-2",500000,2014)
e3= Tecnico("Carlos Pintana","003-3",350000,2002)
e4 = Tecnico("Maria Rios","004-4",350000,2022)
lista_empleados = [e1,e2,e3,e4]

while True:
  print("1. Agregar empleado.")
  print("2. Mostrar empleado.")
  print("3. Salir.")

  opcion = int(input("Elige una opción: "))
  if opcion == 1:
    print("1. Gerente")
    print("2. Técnico")
    tipo_empleado = int(input("Introduce el tipo de empleado según el indice"))
    if tipo_empleado == 1:
      nombre = input("Introduce el nombre del Gerente: ")
      numero_empleado = f"00{len(lista_empleados)+1}-{len(lista_empleados)+1}"
      sueldo = int(input("Introduce el sueldo del Gerente: "))
      entry_year = int(input("Introduce el año de ingreso del Gerente: "))
      nuevo_empleado = Gerente(nombre,numero_empleado,sueldo,entry_year)
      lista_empleados.append(nuevo_empleado)
    else:
      nombre = input("Introduce el nombre del Técnico: ")
      numero_empleado = f"00{len(lista_empleados)+1}-{len(lista_empleados)+1}"
      sueldo = int(input("Introduce el sueldo del Técnico: "))
      entry_year = int(input("Introduce el año de ingreso del Técnico: "))
      nuevo_empleado = Tecnico(nombre,numero_empleado,sueldo,entry_year)
      lista_empleados.append(nuevo_empleado)
  if opcion == 2:
    print("")
    print(f"{'Nombre':<25} {'Numero de empleado':<20} {'Año de ingreso':<17} {'Bono':<6} {'Sueldo base': <15} {'Sueldo total': <15} {'Tipo de empleado': <10}")
    for empleado in lista_empleados:
      empleado.mostrar_datos()
      print("")
    print("")
    
  if opcion == 3:
    break