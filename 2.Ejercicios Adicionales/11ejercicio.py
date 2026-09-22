"""Clase ContadorVotos
Tenga un método registrar_voto(candidato) que guarde en un diccionario la cantidad de votos de cada candidato.
Tenga un método candidato_mas_votado() que retorne el candidato con mayor cantidad de votos.
Tenga un método votos_candidato(candidato) que retorne cuántos votos tiene ese candidato."""

class ContadorVotos:
    def __init__(self):
        self.votos = {}

    def registrar_voto(self,candidato):
        if candidato in self.votos:
            self.votos[candidato] += 1
        else:
            self.votos[candidato] = 1

    def candidato_mas_votado(self):
        mayor = 0
        cantidad_mayor = None
        for candidato, cantidad in self.votos.items():
            if cantidad > mayor:
                mayor = cantidad
                cantidad_mayor = candidato
        return cantidad_mayor

    def votos_cantidato(self,candidato):
        return self.votos.get(candidato,0)

cv = ContadorVotos()

cv.registrar_voto("Nataly")
cv.registrar_voto("Luis")
cv.registrar_voto("Jhordan")
cv.registrar_voto("Jhordan")
cv.registrar_voto("Nataly")
cv.registrar_voto("Sara")
cv.registrar_voto("Nataly")

print(f"Votos: {cv.votos}")
print(f"Candidato mas votado: {cv.candidato_mas_votado()}")
print(f"Votos de Nataly: {cv.votos_cantidato('Nataly')}")