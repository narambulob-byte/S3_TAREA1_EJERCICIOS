"""Gestor de tareas con prioridad
Clase Tareas que: 
(1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); 
(2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta; 
(3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista."""

class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self,descripcion,prioridad):
        self.tareas.append((descripcion,prioridad))

    def tareas_prioritarias(self):
        resultado = []
        for descripcion, prioridad in self.tareas:
            if prioridad.lower() == "alta":
                resultado.append((descripcion,prioridad))
        return resultado

    def eliminar_completada(self,descripcion):
        for tarea in self.tareas:
            if tarea[0].lower() == descripcion.lower():
                self.tareas.remove(tarea)
                return True
        return False

t = Tareas()

t.agregar_tarea("Estudiar Python","alta")
t.agregar_tarea("Ordenar lapiceros","baja")
t.agregar_tarea("Entregar tarea","alta")
t.agregar_tarea("Lavar ropa","media")

print(f"Tareas: {t.tareas}")
print(f"Prioritarias: {t.tareas_prioritarias()}")

print(f"¿Se elimino 'Lavar ropa'? {t.eliminar_completada('Lavar ropa')}")
print(f"¿Se elimino 'bailar'? {t.eliminar_completada('bailar')}")
print(f"Tareas restantes: {t.tareas}")