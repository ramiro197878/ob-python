# En este segundo ejercicio, tendréis que crear un archivo py y dentro
# crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis
# en un archivo y luego lo cargamos.

import pickle


class Vehiculo:

    def __init__(self, color, marca, modelo, puertas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.puertas = puertas


v1 = Vehiculo("Rojo", "Ford", "Ranger", 4)


f = open("archivo.pickle", "wb")
pickle.dump(v1, f)
f.close


f = open("archivo.pickle", "rb")
v2 = pickle.load(f)
f.close()

print(f'El vehiculo es de color {v2.color}')
print(f'De la marca {v2.marca}')
print(f'Modelo {v2.modelo}')
print(f'Y tiene {v2.puertas} puertas')
