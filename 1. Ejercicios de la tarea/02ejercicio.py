"""Contador de palabras únicas
Clase AnalizadorTexto que: 
(1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); 
(2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
(3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios."""

class AnalizadorTexto:
    def __init__(self):
        self.conjunto = set()
        self.lista = []

    def agregar_palabra(self,palabra):
        self.conjunto.add(palabra)
        self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.conjunto)

    def agregar_multiples(self,*args):
        for palabra in args:
            self.agregar_palabra(palabra)

at = AnalizadorTexto()

at.agregar_palabra("Nataly")
at.agregar_palabra("Lizbeth")
at.agregar_palabra("Arambulo")
at.agregar_palabra("Bautista")

print(f"Lista: {at.lista}")
print(f"Conjunto: {at.conjunto}")
print(f"Unicas: {at.contar_palabras()}")

at.agregar_multiples("Hola","mundo","Hola")

print(f"Lista: {at.lista}")
print(f"Palaras unicas: {at.contar_palabras()}")