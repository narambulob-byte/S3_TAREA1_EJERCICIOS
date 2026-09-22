"""GestorCursos
Crea una clase GestorCursos que:

Tenga un método crear_curso(nombre_curso) que cree un curso como una lista vacía dentro de un diccionario.
Tenga un método agregar_estudiante(curso, estudiante) que agregue un estudiante al curso correspondiente.
Tenga un método curso_mayor_estudiantes() que retorne el nombre del curso que tenga más estudiantes."""

class GestorCursos:
    def __init__(self):
        self.cursos = {}

    def crear_curso(self,nombre_curso):
        self.cursos[nombre_curso] = []

    def agregar_estudiante(self,curso,estudiante):
        self.cursos[curso].append(estudiante)

    def curso_mayor_estudiantes(self):
        curso_mayor = None
        mayor_cantidad = 0
        for curso,estudiantes in self.cursos.items():
            if len(estudiantes) > mayor_cantidad:
                mayor_cantidad = len(estudiantes)
                curso_mayor = curso
        return curso_mayor

gc = GestorCursos()

gc.crear_curso("Estructura de datos")
gc.crear_curso("Matematicas discretas")
gc.crear_curso("Modelamiento de software")

gc.agregar_estudiante("Estructura de datos","Nataly")
gc.agregar_estudiante("Estructura de datos","Jhordan")
gc.agregar_estudiante("Estructura de datos","Jazmin")
gc.agregar_estudiante("Matematicas discretas","Paul")
gc.agregar_estudiante("Matematicas discretas","Paulina")
gc.agregar_estudiante("Modelamiento de software","Sofia")

print(f"Cursos: {gc.cursos}")
print(f"Cuso con mayor numero de estudiantes: {gc.curso_mayor_estudiantes()}")