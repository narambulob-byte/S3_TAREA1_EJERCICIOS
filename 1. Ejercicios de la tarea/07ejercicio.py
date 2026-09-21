"""Mapeador de edades
Clase GestorPersonas que: 
(1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario; 
(2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥; 
(3) tenga método edad_promedio() que retorne el promedio de edades."""

class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_personas(self,nombre,edad):
        self.personas[nombre] = edad

    def personas_mayores(self,edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0
        return sum(self.personas.values())/ len(self.personas)

gp = GestorPersonas()

gp.agregar_personas("Nataly",19)
gp.agregar_personas("Jhordan",20)
gp.agregar_personas("Sakael",16)

print(f"Personas: {gp.personas}")
print(f"Mayores o iguales a 18: {gp.personas_mayores(18)}")
print(f"Edad promedio: {gp.edad_promedio():.2f}")
