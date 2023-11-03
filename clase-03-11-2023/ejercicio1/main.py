import pandas as pd
import matplotlib.pyplot as mpl
import random

vdf = pd.read_csv("clientes.csv",index_col="Id")
def obtener_bono(antiguedad):
  if antiguedad >=1 and antiguedad <= 2:
    return "3%"
  elif antiguedad >=3 and antiguedad <=5:
    return "5%"
  elif antiguedad > 5:
    return "10%"
  return "0%"
print("="*20 + "PUNTO 2" + "="*20)
print(vdf)
input("Presiona Enter para continuar: ") 

print("="*20 + "PUNTO 3" + "="*20)
print(vdf.head(3))
input("Presiona Enter para continuar: ") 

print("="*20 + "PUNTO 4" + "="*20)
print(vdf.tail(7))
input("Presiona Enter para continuar: ") 

print("="*20 + "PUNTO 5" + "="*20)
print(vdf.iloc[[5,6,7]])
input("Presiona Enter para continuar: ") 

print("="*20 + "PUNTO 6" + "="*20)
print(vdf.describe())
input("Presiona Enter para continuar: ") 

print("="*20 + "PUNTO 7" + "="*20)
print(vdf[["Edad","NumeroDeTelefono"]])
input("Presiona Enter para continuar: ") 

print("="*20 + "PUNTO 8" + "="*20)
print(vdf[vdf["Plan"] == "A"])
input("Presiona Enter para continuar: ")

print("="*20 + "PUNTO 9" + "="*20)
cantidad_hombres = len(vdf[vdf["Sexo"] == "Masculino"])
cantidad_mujeres = len(vdf[vdf["Sexo"] == "Femenino"])
print(f"La cantidad de mujeres es: {cantidad_mujeres}")
print(f"La cantidad de hombres es: {cantidad_hombres}")
mpl.hist(vdf["Sexo"])
mpl.show()

print("="*20 + "PUNTO 10" + "="*20)
vdf["Bono"] = vdf["Antiguedad"].apply(obtener_bono)
print(vdf)
input("Presiona Enter para continuar: ") 

print("="*20 + "PUNTO 11" + "="*20)
mpl.hist(vdf["Bono"])
mpl.show()

'''
Algo que se me olvido acotar, es la condicional para cumplir este punto
durante la clase solo se busco usando el numero random, pero antes de eso habia que hacer un filtro
para cumplir con las condiciones.
'''
print("="*20 + "PUNTO 12" + "="*20)
vdf_filtrado = vdf[(vdf["Plan"] == "S") & (vdf["Edad"]>18) & (vdf["Antiguedad"] >5)]
# escogemos un numero teniendo en cuenta el tamaño de los filtrados que para este caso son 7
# visualiza este print, y comprobaras el porque se tiene que tener en cuenta solo el tamaño de vdf_filtrado
# print(vdf_filtrado)
elegido = random.randint(1,len(vdf_filtrado))
print("El ganador es:")
print(vdf_filtrado.iloc[elegido])
input("Presiona Enter para continuar: ") 
