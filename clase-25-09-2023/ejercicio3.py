'''
Contador de palabras: Diseña un programa que cuente la cantidad de palabras en un texto ingresado por el usuario.
Utiliza una lista para almacenar las palabras del texto y luego cuenta el número de elementos en la lista.
'''
import re
def contador_palabras(texto):
  patron = r"\b[a-zA-Z]+\b"
  resultado = re.findall(patron,texto)
  return len(resultado)
texto_usuario = input("Ingresa el texto")
print(f"La cantidad de palabras es: {contador_palabras(texto_usuario)}")