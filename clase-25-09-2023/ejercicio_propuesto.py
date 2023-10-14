import re

patron = r"^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$"

if(re.match(patron,"nombredeusuario@dominio.tld")):
  print("correcto")
else:
  print("Incorrecto")