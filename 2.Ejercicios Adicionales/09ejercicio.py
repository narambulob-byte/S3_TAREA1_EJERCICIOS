"""AnalizadorNúmeros
Crea una clase llamada AnalizadorNumeros que:

Tenga un método es_par(numero) que retorne True si el número es par y False si es impar.
Tenga un método contar_por_tipo(numeros) que reciba una lista de números y retorne un diccionario con esta estructura:
{
    "pares": cantidad,
    "impares": cantidad,
    "positivos": cantidad
}
El método debe reutilizar es_par() para determinar si cada número es par o impar.
Tenga un atributo que guarde la lista más larga analizada."""

class AnalizadorNumeros:
    def __init__(self):
        self.lista_mas_larga = []

    def es_par(self,numero):
        return numero % 2 == 0

    def contar_por_tipo(self,numeros):
        resultado =  {
            "pares": 0,
            "impares": 0,
            "positivos": 0
        }
        for numero in numeros:
            if self.es_par(numero):
                resultado["pares"] += 1
            else:
                resultado["impares"] += 1

            if numero > 0:
                resultado["positivos"] += 1

        if len(numeros) > len(self.lista_mas_larga):
            self.lista_mas_larga = numeros

        return resultado

an = AnalizadorNumeros()

resultado = an.contar_por_tipo([1,3,5,7,10,2,6])
print(resultado)
print(f"Lista mas larga: {an.lista_mas_larga}")