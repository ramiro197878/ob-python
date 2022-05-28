# En este ejercicio, tendréis que crear un archivo py donde creéis un
# archivo txt, lo abráis y escribáis dentro del archivo.
# Para ello, tendréis que acceder dos veces al archivo creado.

f = open("file1.txt", "w")
f.write("Pruba de escritura en un archivo.\nSi sale bien despues lo leemos")
f.close()



f = open("file1.txt", "r")
print(f.read())
