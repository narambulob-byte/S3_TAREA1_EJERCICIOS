"""Mapeo de estudiantes a notas
Clase RegistroNotas que: 
(1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
(3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación."""

class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self,estudiante,nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self,nota_minima):
        resultado = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)
        return resultado

    def mejor_estudiante(self):
        if len(self.notas) == 0:
            return None
        mejor_nombre = None
        mejor_nota = -1
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return (mejor_nombre,mejor_nota)

rn = RegistroNotas()

rn.registrar("Nataly",100)
rn.registrar("Jhordan",75)
rn.registrar("Sakael",50)
rn.registrar("Lizbeth",67)

print(f"Notas: {rn.notas}")
print(f"Aprobados con nota >= 70: {rn.estudiantes_aprobados(70)}")

nombre, nota = rn.mejor_estudiante()
print(f"Mejor estudiante: {nombre} con {nota}")