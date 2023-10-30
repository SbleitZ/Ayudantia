# Problema
Desarrolla un Proyecto en Python que haga uso de las librerías necesarias y cumpla con los puntos especificados a continuación. 
Para cada uno de los puntos a partir del punto 2, imprima por pantalla el número de punto y el resultado, luego haga una pausa con una entrada por parte del usuario.
```python
print("PUNTO 2") 
print(dataframe) 
input("Presiona Enter para continuar: ") 
```
1. Descargue el archivo “usuarios.csv” que se encuentra en el mismo sitio de este ejercicio. 
2. Cree un DataFrame a partir de los datos del archivo “usuarios.csv” y muestralo
3. Muestre las primeras 3 filas y las últimas 7 filas del Dataframe
4. Muestra la fila numero 6.
5. Obtenga y muestre un estadístico descriptivo del Dataframe.
6. Muestra solo la columna de Email y NombreCompleto
7. Muestra la cantidad de personas que sean Socios y a continuación los datos de esas personas.
8. Muestra las personas que sean de Chile y su cantidad.
9. Muestra las personas que NO sean de Chile y su cantidad.
10. En base a los puntos 8 y 9 muestra un grafico de barras hacienda la comparativa.
11. Crea una nueva columna en donde puedas categorizar a las personas según su rango etario:
    -	de 19 a 30 años es Joven
    -	de 30 a 60 años es Adulto
    -	de 60 en adelante es Adulto Mayor
    - En caso de no cumplir con ninguna es "Ninguna"
12. Muestra un grafico de barras usando los datos del punto 11.
<image src="./resultados/resultado_12.png" alt="Resultado del punto 12">

13. La empresa requiere hacer un sorteo por su aniversario, para ello necesita escoger de forma aleatoria a un socio y que sea de Chile, una vez encontrado ese socio muestra sus datos de la siguiente manera:
<image src="./resultados/resultado_13.png" alt="Resultado del punto 12">

```python
print("PUNTO 12")
print("El ganador es:")
print(datos_ganador)
input("Presiona Enter para continuar: ") 
```