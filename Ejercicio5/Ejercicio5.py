class Vehiculo():

    def __init__(self, color, ruedas):

        self.color = color
        self.ruedas = ruedas

 

    def __str__(self):

        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self, color, ruedas)

        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

color1 = "Rojo"
ruedas1 = 4
print(color1, ruedas1)
velocidad1 = 120
cilindrada1 = 1000
print(velocidad1, cilindrada1)


c = Coche("azul", 4, 150, 1200)
vehiculos = [color1, ruedas1, velocidad1, cilindrada1]
print(c)

def catalogar(lista):
    for x in lista:
        print(x)
catalogar(vehiculos)


