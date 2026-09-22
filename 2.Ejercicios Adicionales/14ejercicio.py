"""RegistroProductos
Crea una clase RegistroProductos que:

Tenga un método registrar(producto, precio) que guarde cada producto y su precio en un diccionario.
Tenga un método productos_economicos(precio_maximo) que retorne una lista de productos cuyo precio sea menor o igual al máximo indicado.
Tenga un método producto_mas_caro() que retorne el nombre y precio del producto con mayor precio."""

class RegistroProductos:
    def __init__(self):
        self.productos = {}

    def registrar(self,producto,precio):
        self.productos[producto] = precio

    def productos_economicos(self,precio_maximo):
        resultado = []
        for producto,precio in self.productos.items():
            if precio <= precio_maximo:
                resultado.append(producto)
        return resultado

    def producto_mas_caro(self):
        mayor = 0
        producto_mayor = None
        for producto,precio in self.productos.items():
            if precio > mayor:
                mayor = precio
                producto_mayor = producto
        return producto_mayor,mayor

rp = RegistroProductos()

rp.registrar("Mayonesa",100)
rp.registrar("Telefono",350)
rp.registrar("Consola",650)
rp.registrar("Monitor",300)

print(f"Productos: {rp.productos}")
print(f"Productos economicos: {rp.productos_economicos(500)}")

producto,precio = rp.producto_mas_caro()
print(f"Producto mas caro: {producto}")
print(f"Precio: ${precio}")