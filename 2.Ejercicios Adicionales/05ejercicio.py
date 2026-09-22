"""Clase ClasificadorTemperaturas

Debe implementar lo siguiente:

Método es_positiva(temperatura): retorna True si la temperatura es mayor a 0, False en caso contrario.
Método clasificar(*temperaturas): recibe múltiples temperaturas,
reutiliza es_positiva para evaluarlas, y retorna un diccionario {'positivas': [...], 'negativas_o_cero': [...]} con las temperaturas separadas según corresponda.
Método cantidad_por_tipo(): retorna una tupla (cantidad_positivas, cantidad_negativas_o_cero),
basada en los datos ya clasificados."""

class ClasificadorTemperaturas:
    def __init__(self):
        self.datos = {'positivas': [],'negativas_o_cero': []}

    def es_positiva(self,temperatura):
        return temperatura > 0

    def clasificar(self,*temperaturas):
        for temp in temperaturas:
            if self.es_positiva(temp):
                self.datos['positivas'].append(temp)
            else:
                self.datos['negativas_o_cero'].append(temp)
        return self.datos

    def cantidad_por_tipo(self):
        cant_positivas = len(self.datos['positivas'])
        cant_negativas = len(self.datos['negativas_o_cero'])
        return (cant_positivas,cant_negativas)

ct = ClasificadorTemperaturas()

ct.clasificar(10,-1,4,-2,10,-20)

print(f"Temperaturas clasificadas: {ct.datos}")
print(f"Cantidad por tipo: {ct.cantidad_por_tipo()}")