"""Codificador/Decodificador
Clase CodificadorCesar que: 
(1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %); 
(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
(3) tenga un diccionario como atributo para historial de codificaciones."""

class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self,letra,desplazamiento):
        if letra.isupper():
            posicion = ord(letra) - ord('A')
            nueva_posicion = (posicion + desplazamiento) % 26
            return chr(nueva_posicion + ord('A'))
        elif letra.islower():
            posicion = ord(letra) -  ord('a')
            nueva_posicion = (posicion + desplazamiento) % 26
            return chr(nueva_posicion + ord('a'))
        else:
            return letra

    def codificar_palabra(self,palabra,desplazamiento):
         resultado = ""
         for letra in palabra:
                resultado += self.codificar_letra(letra,desplazamiento)
         self.historial[palabra] = resultado
         return resultado

cc = CodificadorCesar()

print(f" 'a' + 1 = {cc.codificar_letra('a',1)}")
print(f" 'z' + 1 = {cc.codificar_letra('z',1)}")
print(f" 'Z' + 3 = {cc.codificar_letra('Z',3)}")

print(f"Codificar 'hola: {cc.codificar_palabra('hola',3)}")
print(f"Codificar 'Python 2026': {cc.codificar_palabra('Python 2026',5)}")

print(f"Historial: {cc.historial}")