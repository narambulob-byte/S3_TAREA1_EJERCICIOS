"""Selector de rango con tuplas
Clase SelectorRango que: 
(1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; 
(2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto."""

class SelectorRango:
    def crear_rango(self,inicio,fin):
        return tuple(range(inicio,fin + 1))

    def elementos_en_multiples_rangos(self,*rangos):
        conjunto = set()
        for inicio, fin in rangos:
            conjunto.update(self.crear_rango(inicio,fin))
        return sorted(conjunto)

sr = SelectorRango()

print(f"Rango de 1 a 5: {sr.crear_rango(1,5)}")
print(f"Rango de 5 a 1: {sr.crear_rango(5,1)}")

combinado = sr.elementos_en_multiples_rangos((1,5),(3,9),(7,17),(16,27))
print(f"Combinado: {combinado}")