"""Asignador de equipos
Clase Equipos que: 
(1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; 
(2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; 
(3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores."""

class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self,nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self,equipo,jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)
            return True
        return False

    def equipo_mayor_integrantes(self):
        if len(self.equipos) == 0:
            return None
        mayor = None
        max_jugadores = -1
        for nombre,jugadores in self.equipos.items():
            if len(jugadores) > max_jugadores:
                max_jugadores = len(jugadores)
                mayor = nombre
        return mayor
        
eq = Equipos()

eq.crear_equipo("Barcelona")
eq.crear_equipo("Emelec")
eq.crear_equipo("Liga de Quito")
eq.crear_equipo("Independiente del valle")

eq.agregar_jugador("Barcelona","Garcia")
eq.agregar_jugador("Barcelona","Diego")
eq.agregar_jugador("Barcelona","Jorge")
eq.agregar_jugador("Emelec","Kendry")
eq.agregar_jugador("Liga de Quito","Piero")
eq.agregar_jugador("Liga de Quito","Santiago")
eq.agregar_jugador("Independiente del valle","Perez")

print(f"Equipos: {eq.equipos}")
print(f"Equipo con mas integrantes: {eq.equipo_mayor_integrantes()}")
print(f"¿Se agrego a un equipo inexistente? {eq.agregar_jugador('España','Juan')}")