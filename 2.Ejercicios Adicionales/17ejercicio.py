"""AgrupadorNotas
Crea una clase AgrupadorNotas que:

Tenga un método clasificar_nota(nota) que retorne la categoría:
"baja" si la nota es menor que 5
"media" si la nota está entre 5 y 7.99
"alta" si la nota es 8 o más.
Tenga un método agrupar_por_categoria(*notas) que retorne un diccionario con:
{categoría: [notas]}
Tenga un método nota_promedio_categoria(categoria) que calcule el promedio de las notas de esa categoría."""

class AgrupadorNotas:
    def __init__(self):
        self.agrupaciones = {}

    def clasificar_nota(self,nota):
        if nota < 5:
            return "baja"
        elif nota < 8:
            return "media"
        else:
            return "alta"

    def agrupar_por_categoria(self,*notas):
        resultado = {}
        for nota in notas:
            categoria = self.clasificar_nota(nota)
            if categoria not in resultado:
                resultado[categoria] = []
            resultado[categoria].append(nota)
        self.agrupaciones = resultado
        return resultado

    def nota_promedio_categoria(self,categoria):
        notas = self.agrupaciones.get(categoria,[])
        if len(notas) == 0:
            return 0
        return sum(notas)/ len(notas)

an = AgrupadorNotas()

resultado = an.agrupar_por_categoria(4,6,7,10,4,7,8,9,9)

print(f"Agrupaciones: {resultado}")
print(f"Promedio de notas altas: {an.nota_promedio_categoria('alta'):.2f}")
print(f"Promedio de notas medias: {an.nota_promedio_categoria('media'):.2f}")
print(f"Promedio de notas bajas: {an.nota_promedio_categoria('baja'):.2f}")