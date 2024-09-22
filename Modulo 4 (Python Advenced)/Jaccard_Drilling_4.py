class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def movimiento(self):
        print(f"{self.nombre} está Caminando")

class Maratonista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def movimiento(self):
        print(f"{self.nombre} está Trotando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def movimiento(self):
        print(f"{self.nombre} está Rodando")

persona = Persona("Persona")
maratonista = Maratonista("Maratonista")
ciclista = Ciclista("Ciclista")

persona.movimiento()
maratonista.movimiento()
ciclista.movimiento()