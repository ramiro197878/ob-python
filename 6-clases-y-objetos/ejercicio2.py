# En este segundo ejercicio, tendréis que crear un programa que tenga una
# clase llamada Alumno que tenga como atributos su nombre y su nota.
# Deberéis de definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota
# y si ha aprobado o no.


class Alumno:

    nombre = str()
    nota = int()

    def nombre_alumno(self, nombre):
        self.nombre = nombre

    def nota_alumno(self, nota):
        self.nota = nota

    def is_aprobado(self):

        if self.nota >= 6:
            return "El alumno %s ha aprobado" % (self.nombre)

        return "El alumno %s no ha aprobado" % (self.nombre)


alumno = Alumno()
alumno.nombre_alumno("Roberto")
alumno.nota_alumno(8)
print(alumno.is_aprobado())
