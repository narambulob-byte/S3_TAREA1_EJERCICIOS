"""Grupo de edades
Clase AgrupadorEdades que: 
(1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); 
(2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
(3) tenga método edad_promedio_categoria(categoria)."""

class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificador_edad(self,edad):
        if edad <= 12:
            return "Niño"
        elif edad <= 17:
            return "Adolescente"
        elif edad <= 64:
            return "Adulto"
        else:
            return "Mayor"

    def agrupar_por_categoria(self, *edades):
        for edad in edades:
            categoria = self.clasificador_edad(edad)
            if categoria not in self.grupos:
                self.grupos[categoria] = []
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self,categoria):
        if categoria not in self.grupos or len(self.grupos[categoria]) == 0:
            return None
        return sum(self.grupos[categoria]) / len(self.grupos[categoria])

ae = AgrupadorEdades()

print(f"Clasificar 7: {ae.clasificador_edad(7)}")
print(f"Clasificar 16: {ae.clasificador_edad(16)}")
print(f"Clasificar 40: {ae.clasificador_edad(40)}")
print(f"Clasificar 70: {ae.clasificador_edad(70)}")

print(f"Agrupadas: {ae.agrupar_por_categoria(7,16,40,70,10,68,35)}")

print(f"Promedio niños: {ae.edad_promedio_categoria('Niño')}")
print(f"Promedio adolescentes: {ae.edad_promedio_categoria('Adolescente')}")
print(f"Promedio adultos: {ae.edad_promedio_categoria('Adulto')}")
print(f"Promedio mayores: {ae.edad_promedio_categoria('Mayor')}")