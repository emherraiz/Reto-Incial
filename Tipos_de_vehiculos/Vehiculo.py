class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def get_ruedas(self):
        return self.ruedas

    def __str__(self):
        return f'Color {self.color}\n {self.ruedas} ruedas\n'
