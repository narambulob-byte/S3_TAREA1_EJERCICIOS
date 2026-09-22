"""AnalizadorFrases
Crea una clase AnalizadorFrases que:

Tenga un método encontrar_palabras_con_letra(texto, letra) que busque palabras que terminen con la letra indicada y retorne una lista.
Tenga un método agrupar_por_longitud(texto) que retorne un diccionario con {longitud: [palabras]}.
Tenga un método palabras_unicas(texto) que retorne las palabras sin repetir utilizando un conjunto."""

class AnalizadorFrases:
    def encontrar_palabras_con_letra(self,texto,letra):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            if palabra.endswith(letra):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self,texto):
        palabras = texto.split()
        resultado = {}
        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in resultado:
                resultado[longitud] = []
            resultado[longitud].append(palabra)
        return resultado

    def palabras_unicas(self,texto):
        palabras = texto.split()
        unicas = set(palabras)
        return unicas

af = AnalizadorFrases()

texto = "gato perro casa gato mesa perro sol"

print(f"Palbras que terminan en 'a': {af.encontrar_palabras_con_letra(texto,'a')}")
print(f"Agrupadas por longitud: {af.agrupar_por_longitud(texto)}")
print(f"Palabras unicas: {af.palabras_unicas(texto)}")