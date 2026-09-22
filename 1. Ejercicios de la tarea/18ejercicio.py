"""Matriz de distancias
Clase CalculadorDistancia que: 
(1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; 
(2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; 
(3) tenga un atributo lista para guardar todas las distancias calculadas."""

import math

class CalculadorDistancia:
    def __init__(self):
        self.historial_distancias = []

    def distancia_euclidiana(self,p1,p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        distancia = math.sqrt(dx ** 2 + dy **2)
        self.historial_distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self,referencia,*puntos):
        if len(puntos) == 0:
            return None
        mas_cercano = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia,punto)
            if menor_distancia is None or distancia < menor_distancia:
                menor_distancia = distancia
                mas_cercano = punto
        return mas_cercano

cd = CalculadorDistancia()

print(f"Distancia (0,0)-(3,4): {cd.distancia_euclidiana((0,0),(3,4))}")

cercano = cd.punto_mas_cercano((0,0),(5,5),(1,1),(10,10),(2,1))
print(f"Punto mas cercano a (0,0): {cercano}")

print(f"Historial de distancias: {cd.historial_distancias}")