"""Clase OrdenadorSecuencia

Debe implementar lo siguiente:

Método duplicar_elementos(lista): retorna una nueva lista donde cada elemento de la lista original aparece dos veces seguidas,
sin usar métodos como *2 directamente sobre elementos ni funciones ya hechas para esto;
hazlo manualmente recorriendo la lista con un bucle.
Método duplicar_multiples(*listas): reutiliza el método anterior para procesar varias listas a la vez,
y retorna un diccionario donde cada clave es la lista original (convertida a algo que pueda usarse como clave) y cada valor es su versión duplicada."""

class OrdenadorSecuencia:
    def duplicar_elementos(self,lista):
        resultado = []
        for elemento in lista:
            resultado.append(elemento)
            resultado.append(elemento)
        return resultado

    def duplicar_multiples(self,*listas):
        resultado = {}
        for lista in listas:
            clave = tuple(lista)
            resultado[clave] = self.duplicar_elementos(lista)
        return resultado

o = OrdenadorSecuencia()

resultado = o.duplicar_multiples([1,2,3],["a","b","c"])
print(f"Resultado: {resultado}")