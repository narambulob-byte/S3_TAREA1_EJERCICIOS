"""Validador de caracteres
Clase AnalizadorString que: 
(1) tenga método solo_vocales(letra) que retorne True si es vocal; 
(2) tenga método contar_por_tipo(texto) que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
(3) tenga atributo que guarde el texto más largo analizado."""

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self,letra):
        vocales ={"a","e","i","o","u","á","é","í","ó","ú"}
        return letra.lower() in vocales

    def contar_por_tipo(self,texto):
        vocales = 0
        consonantes = 0
        digitos = 0

        for caracter in texto:
            if self.solo_vocales(caracter):
                vocales += 1
            elif caracter.isalpha():
                consonantes += 1
            elif caracter.isdigit():
                digitos += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return {'vocales': vocales, 'consonantes': consonantes, 'digitos': digitos}

astr = AnalizadorString()

print(f"¿Es vocal? {astr.solo_vocales('a')}")
print(f"¿Es vocal? {astr.solo_vocales('B')}")
print(f"¿Es vocal? {astr.solo_vocales('E')}")

print(f"Conteo 1: {astr.contar_por_tipo('Hola Mundo 123')}")
print(f"Texto mas largo: {astr.texto_mas_largo}")

print(f"Conteo 2: {astr.contar_por_tipo('Bienvenido')}")
print(f"Texto mas largo: {astr.texto_mas_largo}")

print(f"Conteo 3: {astr.contar_por_tipo('Esta bien no estar bien')}")
print(f"Texto mas largo: {astr.texto_mas_largo}")