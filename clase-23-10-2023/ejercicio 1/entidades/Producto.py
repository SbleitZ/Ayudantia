class Producto:
  def __init__(self,nombre,precio,cantidad):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad
  def mostrar_datos(self):
    print(f"1. Nombre: {self.nombre}")
    print(f"2. Precio: {self.precio}")
    print(f"3. Cantidad: {self.cantidad}")
