"""Clase Biblioteca

Debe implementar lo siguiente:

Método agregar_libro(titulo, paginas): guarda en un diccionario interno la relación {titulo: paginas}.
Método total_paginas(): retorna la suma de todas las páginas de los libros almacenados.
Método libros_por_rango(paginas_min, paginas_max): retorna una lista con los títulos de los libros cuya cantidad de páginas esté dentro del rango indicado (inclusive)."""

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self,titulo,paginas):
        self.libros[titulo] = paginas

    def total_paginas(self):
        return sum(self.libros.values())

    def libros_por_rango(self,paginas_min,paginas_max):
        resultado = []
        for titulo,paginas in self.libros.items():
            if paginas_min <= paginas <= paginas_max:
                resultado.append(titulo)
        return resultado

b = Biblioteca()

b.agregar_libro("La primavero llega pronto",110)
b.agregar_libro("El invierno es largo",200)
b.agregar_libro("La otoño es hermoso",150)
b.agregar_libro("El verano es caluroso",300)

print(f"Total de paginas: {b.total_paginas()}")
print(f"Libros por rango: {b.libros_por_rango(100,250)}")