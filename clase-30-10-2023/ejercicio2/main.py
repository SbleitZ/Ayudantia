import pandas as pd
import matplotlib.pyplot as mpl
import random

vdf = pd.read_csv("usuarios.csv", index_col="Id")
def rango_etario(edad):
  if edad >= 19 and edad <30:
    return "Joven"
  elif edad >= 30 and edad < 60:
    return "Adulto"
  elif edad >=60:
    return "Adulto Mayor"
  return "Ninguna"
print("="*10+"PUNTO 2"+"="*10)
print(vdf)
input("Presiona Enter para continuar: ")
print("="*10+"PUNTO 3"+"="*10)
# Las 3 primeras filas y 7 ultimas filas
print(vdf.head(3))
print(vdf.tail(7))
input("Presiona Enter para continuar: ")

print("="*10+"PUNTO 4"+"="*10)
print(vdf.iloc[6])
input("Presiona Enter para continuar: ")

print("="*10+"PUNTO 5"+"="*10)
# Datos descriptivos
print(vdf.describe())
input("Presiona Enter para continuar: ")

print("="*10+"PUNTO 6"+"="*10)
print(vdf[["NombreCompleto","Email"]])
input("Presiona Enter para continuar: ")

print("="*10+"PUNTO 7"+"="*10)
socios = vdf[vdf["Socio"] == 1]
cantidad_socios = len(socios)
print(f"La cantidad de socios es : {cantidad_socios}")
print(socios)
input("Presiona Enter para continuar: ")

print("="*10+"PUNTO 8"+"="*10)

personas_chile = vdf[(vdf["Pais"] == "Chile")]
cantidad_personas_chile = len(personas_chile)
print(f"La cantidad de personas de Chile es: {cantidad_personas_chile}")
print(personas_chile)
input("Presiona Enter para continuar: ")

print("="*10+"PUNTO 9"+"="*10)

personas_no_chile = vdf[(vdf["Pais"] != "Chile")]
cantidad_personas_no_chile = len(personas_no_chile)
print(f"La cantidad de personas que NO son Chile es: {cantidad_personas_no_chile}")
print(personas_no_chile)
input("Presiona Enter para continuar: ")

print("="*10+"PUNTO 10"+"="*10)
mpl.hist(vdf["Pais"],rwidth=0.8)
mpl.show()

print("="*10+"PUNTO 11"+"="*10)
vdf["RangoEtario"] = vdf["Edad"].apply(rango_etario)

print("="*10+"PUNTO 12"+"="*10)
print("Mostrando grafico...")
mpl.hist(vdf["RangoEtario"])
mpl.show()
print("="*10+"PUNTO 13"+"="*10)
numero_random = random.randint(1,len(vdf))

print("El ganador es: ")
print(vdf.iloc[numero_random])
input("Presiona Enter para continuar: ") 
