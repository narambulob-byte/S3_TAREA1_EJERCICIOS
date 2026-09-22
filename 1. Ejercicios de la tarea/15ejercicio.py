"""Divisores de un número
Clase DivisorFinder que: 
(1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; 
(2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; 
(3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}."""

class DivisorFinder:
    def encontrar_divisores(self,numero):
        divisores = []
        for i in range(1,numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self,numero):
        divisores = self.encontrar_divisores(numero)
        suma_propios = sum(divisores[:-1])
        return suma_propios == numero

    def encontrar_multiples_divisores(self,*numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado

df = DivisorFinder()

print(f"Divisores de 3: {df.encontrar_divisores(3)}")
print(f"Divisores de 10: {df.encontrar_divisores(10)}")

print(f"¿ 6 es perfecto? {df.es_perfecto(6)}")
print(f"¿ 28 es perfecto? {df.es_perfecto(28)}")
print(f"¿ 10 es perfecto? {df.es_perfecto(10)}")

print(f"Multiples: {df.encontrar_multiples_divisores(6,10,28)}")