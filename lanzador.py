from Tipos_de_vehiculos.Vehiculo import Vehiculo
from Tipos_de_vehiculos.Coche import Coche
from Tipos_de_vehiculos.Bicicleta import Bicicleta
from Tipos_de_vehiculos.Motocicleta import Motocicleta
from Tipos_de_vehiculos.Camioneta import Camioneta
from Catalogar import catalogar


Mercedes = Coche('Azul', 4, 180, 25)
Fragoneta = Camioneta('Verde', 6, 100, 20, 190)
BMX = Bicicleta('Blanco', 2, 'Urbana')
KTM = Motocicleta('Amarillo', 2, 'Urbana', 125, 20)

lista = [Mercedes, Fragoneta, BMX, KTM]

