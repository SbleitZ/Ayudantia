from entidades.Empleado import Empleado
class Tecnico(Empleado):
  def __init__(self,nombre,numero_empleado,sueldo,entry_year):
    super().__init__(nombre,numero_empleado,sueldo,entry_year)
  def mostrar_datos(self):
    super().mostrar_datos()
    print(f"{'Técnico':<10}",end="")