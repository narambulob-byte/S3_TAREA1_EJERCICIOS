"""AnalizadorNumeros
Crea una clase AnalizadorNumeros que:

Tenga un método encontrar_multiplos(numero) que retorne una tupla con los múltiplos del número desde 1 hasta 10.
Tenga un método es_multiplo_de_dos(numero) que retorne True si el número es múltiplo de 2.
Tenga un método analizar_multiples(*numeros) que retorne un diccionario {número: tupla_multiplos}."""

class AnalizadorNumeros:
    def encontrar_multiplos(self,numero):
        resultado = []
        for i in range(1,11):
            resultado.append(numero * i)
        return tuple(resultado)

    def es_multiplo_de_dos(self,numero):
        return numero % 2 == 0

    def analizar_multiples(self,*numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_multiplos(numero)
        return resultado

an = AnalizadorNumeros()

print(f"Multiplos de 4: {an.encontrar_multiplos(4)}")
print(f"¿8 es multiplo de 2? {an.es_multiplo_de_dos(8)}")

resultado = an.analizar_multiples(2,4,5)
print(f"Multiplos: {resultado}")