"""Analizador de patrones en textos
Clase AnalizadorPatrones que: 
(1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista; 
(2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; 
(3) tenga método palabras_unicas() usando un conjunto."""

class AnalizadorPatrones:
    def __init__(self):
        self.todas_palabras = []

    def encontrar_palabras(self,texto,patron):
        palabras = texto.split()
        self.todas_palabras.extend(palabras)
        resultado = []
        for palabra in palabras:
            if palabra.lower().startswith(patron.lower()):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self,texto):
        palabras = texto.split()
        self.todas_palabras.extend(palabras)
        resultado = {}
        for palabra in palabras:
            longitud = len(palabra)
            resultado.setdefault(longitud,[]).append(palabra)
        return resultado

    def palabras_unicas(self):
        return sorted(set(self.todas_palabras))

ap = AnalizadorPatrones()

print(f"Palabras con 'pro': {ap.encontrar_palabras('programar en la noche me produce un sueño','pro')}")
print(f"Agrupadas por longitud: {ap.agrupar_por_longitud('el sol y la luna')}")
print(f"Unicas: {ap.palabras_unicas()}")