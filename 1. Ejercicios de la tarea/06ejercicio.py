"""Estadísticas de temperatura
Clase GestorTemperatura que: 
(1) tenga método registrar_temperatura(temp) que guarde en una lista; 
(2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
(3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas."""

class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self,temp):
        self.temperaturas.append(temp)

    def minima(self):
        if len(self.temperaturas) == 0:
            return None
        return min(self.temperaturas)

    def maxima(self):
        if len(self.temperaturas) == 0:
            return None
        return max(self.temperaturas)

    def promedio(self):
        if len(self.temperaturas) == 0:
            return None
        return sum(self.temperaturas)/len(self.temperaturas)

    def registrar_multiples(self,*temps):
        for temp in temps:
            self.registrar_temperatura(temp)

gt = GestorTemperatura()

gt.registrar_temperatura(28.5)
gt.registrar_temperatura(31)

gt.registrar_multiples(20,25,18,30)

print(f"Temperaturas: {gt.temperaturas}")
print(f"Minima: {gt.minima()}")
print(f"Maxima: {gt.maxima()}")
print(f"Promedio: {gt.promedio():.2f}")