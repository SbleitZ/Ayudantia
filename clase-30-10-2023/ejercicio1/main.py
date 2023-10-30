'''
Título,Autor,Género,Año
Una biblioteca muy conocida necesita un programa que le permita leer un archivo txt con la finalidad de poder
agregar y eliminar libros(según el titulo, autor y año), los libros contienen
'''

'''
Título,Autor,Género,Año
Una biblioteca muy conocida necesita un programa que le permita leer un archivo txt con la finalidad de poder
agregar y eliminar libros(según el titulo, autor y año), los libros contienen
'''

archivo= open("libros.txt","r",encoding="utf-8")
archivo.seek(0)
libros = archivo.readlines()

def agregar_libro(titulo,autor,genero,year):
  libro = ','.join([titulo,autor,genero,year])
  print(libro)
  libros.append(libro)
  archivo= open("libros.txt","a",encoding="utf-8")

  archivo.write("\n"+libro)

def eliminar_libro(titulo,autor,year):
  i = 0

  # encontramos la linea del libro a eliminar
  encontrado = False
  for libro in libros:
    titulo_txt,autor_txt,genero_txt,year_txt = libro.split(",")
    if (titulo_txt == titulo) and (autor_txt == autor) and (year == year_txt.strip()):
      encontrado = True
      break
    i+=1
  if(encontrado):
    print(i)
    libros.pop(i)
    libro_nuevo = open("libros.txt","w",encoding="utf-8")
    # se hace  el guardado
    for w in libros:
      libro_nuevo.write(w.strip()+"\n")
  else:
    print("El libro no ha sido encontrado")
  
while True:
  print("1. Agregar libro.")
  print("2. Eliminar libro.")
  print("3. Mostrar libros.")
  print("4. Finalizar programa.")
  opcion = int(input("Elige una opción: "))
# Título,Autor,Género,Año
  if opcion == 1:
    titulo = input("Ingresa el titulo: ")
    autor = input("Ingresa el autor: ")
    genero = input("Ingresa el genero: ")
    year = input("Ingresa el año: ")
    agregar_libro(titulo,autor,genero,year)
    print("Libro agregado exitosamente.")
  elif opcion == 2:
    titulo = input("Ingresa el titulo del libro a eliminar: ")
    autor = input("Ingresa el autor del libro a eliminar: ")
    year = input("Ingresa el año: ")
    eliminar_libro(titulo,autor,year)
  elif opcion == 3:
    print("Libros...")

    for libro in libros:
      print(libro.strip())
    
  elif opcion == 4:
    break
  else:
    print("La opción ingresada no es valida")

