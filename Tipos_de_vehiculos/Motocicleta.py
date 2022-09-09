class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'{Bicicleta.__str__(self)} {self.velocidad} km/h\n {self.cilindrada} cc\n'
