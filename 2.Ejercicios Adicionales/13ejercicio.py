"""MezcladorNombres
Crea una clase MezcladorNombres que:

Tenga un método alternar(lista1, lista2) que retorne una lista alternando los elementos de ambas listas.
Tenga un método alternar_multiples(*listas) que reutilice el método alternar() para combinar varias listas."""

class MezcladorNombres:
    def alternar(self,lista1,lista2):
        resultado = []
        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])
        return resultado

    def alternar_multiples(self,*listas):
        resultado = []
        for i in range(len(listas[0])):
            for lista in listas:
                resultado.append(lista[i])
        return resultado

mn = MezcladorNombres()

lista1 = ["Nataly","Lizbeth","Sara","Noemi"]
lista2 = ["Daniel","Jhordan","David","Noelia"]

print(f"Listas alternadas: {mn.alternar(lista1,lista2)}")

lista3 = ["Andrea","Andres","Alex","Alexandra"]
print(f"Alternar entre varias listas: {mn.alternar_multiples(lista1,lista2,lista3)}")