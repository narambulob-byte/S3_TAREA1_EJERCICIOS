"""Contador de frecuencia
Clase ContadorFrecuencia que: 
(1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones; 
(2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia; 
(3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece."""

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self,elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] +=1
        else:
            self.frecuencias[elemento] = 1

    def frecuencia_elemento(self,elemento):
        return self.frecuencias.get(elemento,0)

    def elemento_mas_frecuente(self):
        if len(self.frecuencias) == 0:
            return None
        mas_frecuente = None
        max_frecuencia = 0
        for elemento,cantidad in self.frecuencias.items():
            if cantidad > max_frecuencia:
                max_frecuencia = cantidad
                mas_frecuente = elemento
        return mas_frecuente

cf = ContadorFrecuencia()

for palabra in ["python","clase","python","objeto","python","clase"]:
    cf.agregar_elemento(palabra)

print(f"Frecuencias: {cf.frecuencias}")
print(f"Mas frecuente: {cf.elemento_mas_frecuente()}")
print(f"Veces 'python' {cf.frecuencia_elemento('python')}")
print(f"Veces 'clase' {cf.frecuencia_elemento('clase')}")
print(f"Veces 'java' {cf.frecuencia_elemento('java')}")