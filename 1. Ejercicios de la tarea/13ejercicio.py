"""Combinador de listas
Clase CombinadorListas que: 
(1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; 
(2) tenga método intercalar_multiples(*listas) que reutilice para varias listas."""

class CombinadorListas:
    def intercalar(self,lista1,lista2):
        resultado = []
        largo_mayor = max(len(lista1),len(lista2))
        for i in range(largo_mayor):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self,*listas):
        if len(listas) == 0:
            resultado = listas[0]
            for lista in listas[1:]:
                resultado = self.intercalar(resultado,lista)
            return resultado

cl = CombinadorListas()

print(f"Intercalado (mismo tamaño): {cl.intercalar([1,3,5],[2,4,6])}")
print(f"Intercalado (distinto tamaño): {cl.intercalar([1,2,3],['a','b','c'])}")

print(f"Multiples: {cl.intercalar_multiples([1,4],[2,7],[7,10])}")