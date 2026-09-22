"""Clase Peliculas que:

Tenga un método agregar_pelicula(titulo, genero) que guarde cada película en una lista de tuplas (titulo, genero).
Tenga un método peliculas_accion() que retorne solamente las películas cuyo género sea "Accion".
Tenga un método eliminar_pelicula(titulo) que elimine de la lista la película indicada."""

class Peliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self,titulo,genero):
        self.peliculas.append((titulo,genero))

    def peliculas_accion(self):
        resultado = []
        for pelicula in self.peliculas:
            if pelicula[1] == "Accion":
                resultado.append(pelicula)
        return resultado

    def eliminar_pelicula(self,titulo):
        for pelicula in self.peliculas:
            if pelicula[0] == titulo:
                self.peliculas.remove(pelicula)
                break

p = Peliculas()

p.agregar_pelicula("Your name","Romance")
p.agregar_pelicula("Amor de gato","Fantasia")
p.agregar_pelicula("Titanic","Romance")
p.agregar_pelicula("Avatar","Accion")

print(f"Peliculas: {p.peliculas}")
print(f"Peliculas de accion: {p.peliculas_accion()}")

p.eliminar_pelicula("Titanic")
print(f"Peliculas actualizadas: {p.peliculas}")