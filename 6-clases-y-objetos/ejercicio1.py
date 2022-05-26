#En este ejercicio vais a crear la clase Vehículo la cual tendrá
#los siguientes atributos:

#Color
#Ruedas
#Puertas

#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y
#tendrá los siguientes atributos:

#Velocidad
#Cilindrada

#Por último, tendrás que crear un objeto de la clase Coche
#y mostrarlo por consola.

class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return """El vehículo es de color %s, tiene %s puertas \
y %s ruedas.""" % (self.color, self.puertas, self.ruedas)



class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindradas):
        Vehiculo.__init__(self, color, ruedas, puertas)

        self.velocidad = velocidad
        self.cilindradas = cilindradas


    def __str__(self):
        return """El vehículo es de color %s, tiene %s puertas \
y %s ruedas. La velocidad maximas es de %s km/h y tiene %s cilindradas""" \
% (self.color, self.puertas, self.ruedas, self.velocidad, self.cilindradas)


vehiculo = Vehiculo("Rojo", 4, 5)
print(vehiculo)

coche = Coche("verde", 4, 4, 150, 2000)
print(coche)
