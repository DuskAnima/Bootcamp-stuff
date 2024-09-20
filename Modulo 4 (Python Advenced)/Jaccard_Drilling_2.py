class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self._nombre = nombre
        self._apellidos = apellidos
        self._sexo = sexo
        self._edad = edad
        self._estatura = estatura
        self._peso = peso

    @property
    def edad(self):
        print("Su edad actual es:")
        return self._edad
        
    @edad.setter
    def edad(self, nueva_edad):
        print("se ha cambiado la edad")
        self._edad = nueva_edad

    @property
    def apellidos(self):
        print("Su apellido es:")
        return self._apellidos
    
    @apellidos.setter
    def apellidos(self, nuevo_apellido):
        print("Se ha cambiado el apellido")
        self._apellidos = nuevo_apellido

persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)

persona_1.edad = 21
print(persona_1.edad)

persona_2.apellidos = "Santiago"
print(persona_2.apellidos)