from Tipos_de_vehiculos.Vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'{Vehiculo.__str__(self)} {self.velocidad} km/h\n {self.cilindrada} cc\n'
