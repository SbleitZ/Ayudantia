from entidades.Producto import Producto
class OrdenCompra():
  def __init__(self):
    self.lista_productos = []
  def agregar_producto(self,nombre,precio,cantidad):
    nuevo_producto = Producto(nombre,precio,cantidad)
    self.lista_productos.append(nuevo_producto)
    print("El producto ha sido agregado.")
  def calcular_precio_total(self):
    total = 0
    for producto in self.lista_productos:
      total+= producto.precio * producto.cantidad
    return total
  def mostrar_precio_total(self):
    print(f"Total a pagar : {self.calcular_precio_total():.2f}")
  def mostrar_productos(self):
    if len(self.lista_productos) == 0:
      print("Actualmente tienes 0 productos.")
      return
    i = 1
    for producto in self.lista_productos:
      print(f"Producto {i}")
      producto.mostrar_datos()
      i+=1