class Persona:
    def __init__(self, nombre, apellido, anio):
        self.nombre = nombre
        self.apellido = apellido
        self.anio = anio

class Departamento:
    def __init__(self, nombre_depto, nombre_corto_depto) -> None:
        self.nombre_depto = nombre_depto
        self.nombre_corto_depto = nombre_corto_depto

class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anio, nombre_depto, nombre_corto_depto, salario):
        Persona.__init__(self, nombre, apellido, anio)
        Departamento.__init__(self, nombre_depto, nombre_corto_depto)
        self.salario = salario

trabajador = Trabajador("Juan", "Perez", 2005, "Ingeniería en Software", "IS", 20000)

print(trabajador.__dict__)
print(isinstance(trabajador, Persona))
print(isinstance(trabajador, Departamento))
print(isinstance(trabajador, Trabajador))