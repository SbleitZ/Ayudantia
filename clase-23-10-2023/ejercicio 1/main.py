'''
Crear el entorno de archivos, es decir, producto.py, ordencompra.py y main.py que es donde manejaras todo
Luego de eso crea las respectivas clases
luego de eso crea los datos falsos 
luego de eso crea la funcionalidad principal que te estan pidiendo
'''
from entidades.OrdenCompra import OrdenCompra
  
w = OrdenCompra()
while True:
  print(f"1. Agregar producto.")
  print(f"2. Mostrar mis productos.")
  print(f"3. Finalizar compra.")
  opcion = int(input("Elige una opción: "))

  if opcion == 1:
    nombre = input("Introduce el nombre del producto: ")
    precio = int(input(f"Introduce el precio : "))
    cantidad = int(input(f"Introduce la cantidad:  "))
    w.agregar_producto(nombre,precio,cantidad)
  elif opcion == 2:
    w.mostrar_productos()
    w.mostrar_precio_total()
  elif opcion == 4:
    w.mostrar_precio_total()
    break
  else:
    print("La opción elegida no existe.")
# w.agregar_producto("Lechuga",500,2)
# w.agregar_producto("Platano",300,3)
# w.agregar_producto("Manzana",300,4)
# w.mostrar_precio_total()