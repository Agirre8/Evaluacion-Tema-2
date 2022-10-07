class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def calificacion (nombre, nota):
        if nota<5:
            print("el alumno:", nombre, "ha suspendido")
        else:
            return print("El alumno:", nombre, "ha aprobado")

    calificacion ("Iñigo",3)