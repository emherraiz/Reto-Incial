class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def get_ruedas(self):
        return self.ruedas

    def __str__(self):
        return f'Color {self.color}\n {self.ruedas} ruedas\n'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'{Vehiculo.__str__(self)} {self.velocidad} km/h\n {self.cilindrada} cc\n'

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f'{Coche.__str__(self)} {self.carga} kg\n'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{Vehiculo.__str__(self)} Tipo {self.tipo}\n'

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f'{Bicicleta.__str__(self)} {self.velocidad} km/h\n {self.cilindrada} cc\n'


Mercedes = Coche('Azul', 4, 180, 25)
Fragoneta = Camioneta('Verde', 6, 100, 20, 190)
BMX = Bicicleta('Blanco', 2, 'Urbana')
KTM = Motocicleta('Amarillo', 2, 'Urbana', 125, 20)

lista = [Mercedes, Fragoneta, BMX, KTM]

def catalogar(lista, ruedas = 0):
    if ruedas == 0:
        for i in lista:
            print(i)
    else:
        suma = 0
        for i in lista:
            if i.get_ruedas() == ruedas:
                suma +=1

        print(f'Se han encontrado {suma} vehiculos con {ruedas} ruedas')

catalogar(lista, 2)
