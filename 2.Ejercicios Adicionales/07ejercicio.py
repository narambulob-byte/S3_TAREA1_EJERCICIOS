"""GestorProductos 
Crea una clase llamada GestorProductos que:

Tenga un método agregar_producto(nombre, precio) que guarde los productos en un diccionario,
usando el nombre como clave y el precio como valor.
Tenga un método productos_caros(precio_minimo) que retorne una lista con los nombres de los productos cuyo precio sea mayor o igual al precio mínimo indicado.
Tenga un método precio_promedio() que retorne el promedio de los precios de todos los productos registrados."""

class GestorProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self,nombre,precio):
        self.productos[nombre] = precio

    def productos_caros(self,precio_minimo):
        resultado = []
        for nombre,precio in self.productos.items():
            if precio >= precio_minimo:
                resultado.append(nombre)
        return resultado

    def precio_promedio(self):
        return sum(self.productos.values())/ len(self.productos)

gp = GestorProductos()

gp.agregar_producto("Laptop",700)
gp.agregar_producto("Mouse",50)
gp.agregar_producto("Pc",1000)
gp.agregar_producto("Tablet",800)

print(f"Productos: {gp.productos}")
print(f"Prouctos caros: {gp.productos_caros(500)}")
print(f"Precio promedio: {gp.precio_promedio()}")