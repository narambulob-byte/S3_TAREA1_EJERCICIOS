"""Clase GestorInventario
Debe implementar lo siguiente:
Método validar_cantidad(cantidad): retorna True si la cantidad es mayor o igual a 0 y menor o igual a 1000, False en caso contrario.
Método agregar_productos(*args): recibe múltiples cantidades de productos, valida cada una usando el método anterior,
agrega solo las cantidades válidas a una lista interna, y retorna esa lista.
Método total_unidades(): retorna la suma total de todas las cantidades almacenadas en la lista interna."""

class GestorInventario:
    def __init__(self):
        self.cantidades = []

    def validar_cantidad(self,cantidad):
        return 0 <= cantidad <= 1000

    def agregar_productos(self,*args):
        for cantidad in args:
            if self.validar_cantidad(cantidad):
                self.cantidades.append(cantidad)
        return self.cantidades

    def total_unidades(self):
        if len(self.cantidades) == 0:
            return 0
        return sum(self.cantidades)

inv = GestorInventario()

inv.agregar_productos(100,200,50,300)

print(f"Inventario: {inv.cantidades}")
print(f"Total de unidades: {inv.total_unidades()}")