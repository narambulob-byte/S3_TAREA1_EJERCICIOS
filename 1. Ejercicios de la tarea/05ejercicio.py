"""Detector de números pares e impares
Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False; 
(2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par; 
(3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares)."""

class AnalizadorNumeros:
    def __init__(self):
        self.resultado = {'pares':[], 'impares':[]}

    def es_par(self,numero):
        return numero % 2 == 0

    def separar(self,*numeros):
        self.resultado = {'pares':[],'impares':[]}
        for numero in numeros:
            if self.es_par(numero):
                self.resultado['pares'].append(numero)
            else:
                self.resultado['impares'].append(numero)
        return self.resultado

    def cantidad_pares_impares(self):
        cant_pares = len(self.resultado['pares'])
        cant_impares = len(self.resultado['impares'])
        return(cant_pares,cant_impares)

an = AnalizadorNumeros()

print(an.separar(1,2,3,4,5))
print(f"La cantidad de pares e impares son: {an.cantidad_pares_impares()}")