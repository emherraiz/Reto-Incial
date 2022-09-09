from Tipos_de_vehiculos.Vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{Vehiculo.__str__(self)} Tipo {self.tipo}\n'
