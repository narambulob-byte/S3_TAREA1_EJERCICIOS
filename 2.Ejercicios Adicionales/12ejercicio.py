"""SelectorEdades
Crea una clase SelectorEdades que:

Tenga un método crear_rango_edades(inicio, fin) que retorne una tupla con las edades dentro de ese rango.
Tenga un método edades_en_multiples_rangos(*rangos) que reciba varias tuplas (inicio, fin) y 
retorne una lista combinada sin duplicados, utilizando un conjunto."""

class SelectorEdades:
    def crear_rango(self,inicio,fin):
        return tuple(range(inicio, fin +1))

    def edades_en_multiples_rangos(self,*rangos):
        edades = set()
        for inicio,fin in rangos:
            for edad in range(inicio,fin + 1):
                edades.add(edad)
        return list(edades)

se = SelectorEdades()

print(f"Rango de edades: {se.crear_rango(18,21)}")

resultado = se.edades_en_multiples_rangos(
    (18,21),
    (20,23),
    (25,27)
)

print(f"Edades sin duplicados: {resultado}")