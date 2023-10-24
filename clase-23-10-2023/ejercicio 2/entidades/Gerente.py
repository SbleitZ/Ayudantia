from entidades.Empleado import Empleado
class Gerente(Empleado):
  def __init__(self,nombre,numero_empleado,sueldo,entry_year):
    super().__init__(nombre,numero_empleado,sueldo,entry_year)
  def mostrar_datos(self):
    super().mostrar_datos()
    print(f"{'Gerente':<10}",end="")