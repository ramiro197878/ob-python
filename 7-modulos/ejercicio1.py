# En este ejercicio tendréis que crear un módulo que contenga las operaciones
# básicas de una calculadora: sumar, restar, multiplicar y dividir.
# Este módulo lo importaréis a un archivo python y llamaréis a las funciones
# creadas. Los resultados tenéis que mostrarlos por consola.

from calculos import operaciones

a = 3
b = 0

sumar = operaciones.suma(a, b)
restar = operaciones.resta(a, b)
multiplicar = operaciones.multiplica(a, b)
dividir = operaciones.divide(a, b)

print("La resultado de la operacion {} + {} = {}".format(a, b, sumar))
print("La resultado de la operacion {} - {} = {}".format(a, b, restar))
print("La resultado de la operacion {} * {} = {}".format(a, b, multiplicar))
print("La resultado de la operacion {} / {} = {}".format(a, b, dividir))
