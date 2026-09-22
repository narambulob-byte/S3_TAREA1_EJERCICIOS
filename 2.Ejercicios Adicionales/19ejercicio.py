"""Biblioteca
Crea una clase Biblioteca que:

Tenga un método agregar_libro(titulo, cantidad) que guarde la cantidad de ejemplares en un diccionario.
Tenga un método prestar_libro(titulo, cantidad) que disminuya la cantidad y retorne True si hay suficientes ejemplares. Si no hay suficientes, debe retornar False.
Tenga un método libros_pocos_ejemplares(minimo) que retorne una lista con los títulos cuya cantidad sea menor que minimo."""

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self,titulo,cantidad):
        self.libros[titulo] = cantidad

    def prestar_libro(self,titulo,cantidad):
        if titulo in self.libros and self.libros[titulo] >= cantidad:
            self.libros[titulo] -= cantidad
            return True
        return False

    def libros_pocos_ejemplares(self,minimo):
        resultado = []
        for titulo, cantidad in self.libros.items():
            if cantidad < minimo:
                resultado.append(titulo)
        return resultado

b = Biblioteca()

b.agregar_libro("Harry Poter",10)
b.agregar_libro("La bella y la bestia",6)
b.agregar_libro("Cenicienta",12)
b.agregar_libro("Yor name",5)

print(f"Libros: {b.libros}")

print(f"¿Se prestaron 2 libros de Cenicienta? {b.prestar_libro('Cenicienta',2)}")
print(f"Libros actuales: {b.libros}")

print(f"Libros con pocos ejemplares: {b.libros_pocos_ejemplares(6)}")