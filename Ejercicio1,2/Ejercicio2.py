class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def calificacion (nombre, nota):
        if nota<5:
            print("El alumno:", nombre, "ha suspendido")
        else:
            return print("El alumno:", nombre, "ha aprobado")
    def __str__(self): 
        return print(self.nombre, self.nota)
alumno1=Alumno("Eustaquio",6)
print(alumno1)

    
