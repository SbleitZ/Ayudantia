'''
Eliminación de duplicados: Crea un programa que elimine los elementos duplicados de una lista ingresada por el usuario.
Utiliza conjuntos para eliminar los duplicados y luego muestra la lista resultante sin elementos repetidos.
'''

estado = False
lista_elementos = []

while True:
  elemento = input("Introduce el elemento que quieres añadir: ")
  lista_elementos.append(elemento)
  print("Elemento agregado.\n")
  salida = input("¿Quieres seguir añadiendo elementos? (Y/N): ").lower()
  if(salida == "y"):
    break

print(f"Lista de elementos original: {lista_elementos}")
lista_no_duplicada = list(set(lista_elementos))
print(f"Lista de elementos sin duplicar: {lista_no_duplicada}")
