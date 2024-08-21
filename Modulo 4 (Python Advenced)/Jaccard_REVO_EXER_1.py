class animal():
    def __init__(self, nombre, raza, edad, peso) -> None:
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    def comer (self):
        self.peso
    def caminar(sellf):
        pass
    def dormir(self):
        pass
    def __str__(self):
        return (f"Nombre: {self.nombre}. Raza: {self.raza}. Edad: {self.edad} años. Peso: {self.peso}kg")

perro = animal("Brando", "San Bernardo", 3, 30)
gato = animal("Roll", "Persa", 4, 3)

print(perro)
print(gato)