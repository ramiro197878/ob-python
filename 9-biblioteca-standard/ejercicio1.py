# Crea un script que le pida al usuario una lista de países
# (separados por comas). Éstos se deben almacenar en una lista. No debería
# haber países repetidos (haz uso de set). Finalmente, muestra por consola
# la lista de países ordenados alfabéticamente y separados por comas.

print("Lista de paises ordenados")

paises = input("Ingrese la lista de paises separados por coma: ")

ordenar = set(paises.replace(',', '').split())

print(sorted(ordenar))
