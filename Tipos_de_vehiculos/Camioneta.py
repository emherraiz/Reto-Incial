from Tipos_de_vehiculos.Vehiculo import Vehiculo
from Tipos_de_vehiculos.Coche import Coche
class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f'{Coche.__str__(self)} {self.carga} kg\n'
