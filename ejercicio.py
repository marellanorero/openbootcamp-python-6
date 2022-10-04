class Alumno:
    def __init__(self):
        self.nota = 4

    def resultado(self, valor):
        self.nota = valor
        if valor > 4:
            print(valor, "Felicidades, estás aprobado")
        else:
            print(valor, "Lo siento, no estás aprobado")

laura = Alumno()
laura.resultado(5)


