"""Gestor de compras con totales
Clase CarroCompras que: 
(1) tenga método agregar_articulo(nombre, precio) que guarde en un diccionario {nombre: precio}; 
(2) tenga método total_carrito() que retorne la suma de todos los precios; 
(3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango."""

class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self,nombre,precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self,precio_min,precio_max):
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado

c = CarroCompras()

c.agregar_articulo("Pan",2.75)
c.agregar_articulo("Leche",3.25)
c.agregar_articulo("Laptop",1500)

print(f"Articulos: {c.articulos}")
print(f"Total: ${c.total_carrito():.2f}")
print(f"Articulos entre el rango: {c.articulos_por_rango(2.50,10.00)}")