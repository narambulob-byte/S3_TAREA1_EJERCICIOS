"""Inventario de productos
Clase Inventario que: 
(1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
(2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo."""

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self,producto,cantidad):
        if producto not in self.stock:
            self.stock[producto] = 0
        self.stock[producto] += cantidad

    def restar_stock(self,producto,cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self,minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado

inv = Inventario()

inv.agregar_stock("Manzana",12)
inv.agregar_stock("Pizza",20)
inv.agregar_stock("Uva",10)
inv.agregar_stock("Mermelada",11)

print(f"Stock: {inv.stock}")

print(f"¿Restar 5 manzanas? {inv.restar_stock('Manzana',5)}")
print(f"¿Restar 2 uvas? {inv.restar_stock('Uva',2)}")

print(f"Stock actualizado: {inv.stock}")
print(f"Bajo stock < 10: {inv.productos_bajo_stock(10)}")