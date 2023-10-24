class Empleado:
  def __init__(self,nombre,numero_empleado,sueldo,entry_year):
    self.nombre = nombre
    self.numero_empleado = numero_empleado
    self.sueldo = sueldo
    self.entry_year = entry_year
  def calcular_bono(self):
    # 2010
    if (2023 - self.entry_year) < 5 and (2023 - self.entry_year) <= 10:
      # el 5 porciento de bono
      return 0.05 * self.sueldo
    elif (2023 - self.entry_year) < 10 and (2023 - self.entry_year) <= 15:
      return 0.1 * self.sueldo
    else:
      return 0
  def mostrar_datos(self):
    empleado_info = f"{self.nombre:<25} {self.numero_empleado:<20} {self.entry_year:<17} {str(int((self.calcular_bono()/self.sueldo)*100))+str('%'):<6} ${self.sueldo:<15} {self.sueldo+self.calcular_bono():<15}"
    print(empleado_info,end="")
    
    # print(f"Nombre: {self.nombre}")
    # print(f"Numero de empleado: {self.numero_empleado}")
    # print(f"Año de ingreso: {self.entry_year}")
    # print(f"Bono {(self.calcular_bono()/self.sueldo)*100:.0f}%: {self.calcular_bono()}")
    # print(f"Sueldo base: {self.sueldo}")
    # print(f"Sueldo con bono: {self.sueldo+self.calcular_bono()}")