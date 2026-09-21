"""Detector de números pares e impares
Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False; 
(2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par; 
(3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares)."""

class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self,numero):
        return numero % 2 == 0

    def separar(self,*numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)
        return {'pares': self.pares, 'impares': self.impares}

    def cantidad_pares_impares(self):
        return (len(self.pares),len(self.impares))

an = AnalizadorNumeros()

print(f"¿Es par? {an.es_par(4)}")
print(f"¿Es par? {an.es_par(7)}")

resultado = an.separar(1,2,3,4,5,6,7)
print(f"Pares e impares: {resultado}")

pares, impares = an.cantidad_pares_impares()
print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")

print(f"Cantidad (pares,impares): {an.cantidad_pares_impares()}")