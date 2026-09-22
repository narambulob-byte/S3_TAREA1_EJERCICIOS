"""TraductorNumeros
Crea una clase TraductorNumeros que:

Tenga un método duplicar_numero(numero) que retorne el número multiplicado por 2.
Tenga un método duplicar_lista(numeros) que reutilice duplicar_numero() para transformar todos los números de una lista.
Tenga un diccionario como atributo llamado historial para guardar las listas originales y sus resultados."""

class TraductorNumeros:
    def __init__(self):
        self.historial = {}

    def duplicar_numero(self,numero):
        return numero * 2

    def duplicar_lista(self,numeros):
        resultado = []
        for numero in numeros:
            resultado.append(self.duplicar_numero(numero))
        self.historial[tuple(numeros)] = resultado
        return resultado

tn = TraductorNumeros()

lista1 = [2,3,4,5,6]
lista2 = [2,20,10]

print(f"Original: {lista1}")
print(f"Duplicados: {tn.duplicar_lista(lista1)}")

print(f"Original: {lista2}")
print(f"Duplicados: {tn.duplicar_lista(lista2)}")

print(f"Historial: {tn.historial}")