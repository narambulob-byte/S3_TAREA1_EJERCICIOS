"""Clase GestorNotas

Crea una clase llamada GestorNotas que:

Tenga un atributo que almacene las notas de los estudiantes en una lista.
Tenga un método registrar_nota(nota) que agregue una nueva nota a la lista.
Tenga un método menor() que devuelva la nota más baja.
Tenga un método mayor() que devuelva la nota más alta.
Tenga un método promedio() que calcule y devuelva el promedio de todas las notas.
Tenga un método registrar_multiples(*notas) que permita registrar varias notas y que reutilice el método registrar_nota()."""

class GestorNotas:
    def __init__(self):
        self.notas = []

    def registrar_nota(self,nota):
        self.notas.append(nota)

    def menor(self):
        return min(self.notas)

    def mayor(self):
        return max(self.notas)

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def registrar_multiples(self,*notas):
        for nota in notas:
            self.registrar_nota(nota)

gn = GestorNotas()

gn.registrar_nota(10)
gn.registrar_nota(8)
gn.registrar_nota(7)

gn.registrar_multiples(9,10,7,5)

print(f"Notas: {gn.notas}")
print(f"Nota menor: {gn.menor()}")
print(f"Nota mayor: {gn.mayor()}")
print(f"Promedio: {gn.promedio()}")