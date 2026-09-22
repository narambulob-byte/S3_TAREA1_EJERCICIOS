"""CalculadorTemperaturas
Crea una clase CalculadorTemperaturas que:

Tenga un método diferencia_temperatura(t1, t2) que reciba dos temperaturas y calcule la diferencia absoluta entre ellas.
Tenga un método temperatura_mas_cercana(referencia, *temperaturas) que retorne la temperatura más cercana a la referencia.
Tenga un atributo tipo lista para guardar todas las diferencias de temperatura calculadas."""

class CalculadorTemperaturas:
    def __init__(self):
        self.diferencias = []

    def diferencia_temperatura(self,t1,t2):
        diferencia = abs(t1-t2)
        self.diferencias.append(diferencia)
        return diferencia

    def temperatura_mas_cercana(self,referencia,*temperaturas):
        mas_cercana = temperaturas[0]
        for temperatura in temperaturas:
            diferencia_actual = self.diferencia_temperatura(referencia,temperatura)
            diferencia_cercana = abs(referencia - mas_cercana)
            if diferencia_actual < diferencia_cercana:
                mas_cercana = temperatura
        return mas_cercana

ct = CalculadorTemperaturas()

print(f"Diferencia entre temperaturas: {ct.diferencia_temperatura(10,20)}")

resultado = ct.temperatura_mas_cercana(25,18,22,45,30)

print(f"Temperatura mas cercana: {resultado}")
print(f"Diferencias calculas: {ct.diferencias}")