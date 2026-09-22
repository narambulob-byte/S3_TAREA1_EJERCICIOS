"""Clase RegistroVisitantes

Debe implementar lo siguiente:

Método agregar_visitante(nombre): agrega el nombre a un conjunto (set) interno para evitar duplicados,
y también lo agrega a una lista interna para mantener el orden en que fueron llegando.
Método contar_unicos(): retorna cuántos visitantes únicos (sin duplicados) han sido registrados.
Método agregar_varios(*args): recibe múltiples nombres, y reutiliza el método agregar_visitante para agregarlos uno por uno."""

class RegistroVisitantes:
    def __init__(self):
        self.visitantes = []
        self.unicos = set()

    def agregar_visitante(self,nombre):
        self.unicos.add(nombre)
        self.visitantes.append(nombre)

    def contar_unicos(self):
        return len(self.unicos)

    def agregar_varios(self,*args):
        for nombre in args:
            self.agregar_visitante(nombre)

rv = RegistroVisitantes()

rv.agregar_varios("Nataly","Jhordan","Sara","Keyla","Nataly","Sara")

print(f"Lista completa: {rv.visitantes}")
print(f"Unicos: {rv.unicos}")
print(f"Total de unicos: {rv.contar_unicos()}")