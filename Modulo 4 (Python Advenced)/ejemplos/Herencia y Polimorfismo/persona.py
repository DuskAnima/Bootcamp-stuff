class Persona:
    def __init__(self, nombre, apellidos, cedula):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula

    def get_tipo(self):
        print("Soy del tipo persona")

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre} \nApellidos: {self.apellidos} \nCédula: {self.cedula}")
    
    def __str__(self):
        return f'Nombre: {self.nombre} \nApellidos: {self.apellidos} \nCédula: {self.cedula}'
    
class Supervisor(Persona):
    def __init__(self, nombre, apellidos, cedula, zona):
        super().__init__(nombre, apellidos, cedula)
        self.zona = zona
    
    def get_tipo(self):
        print("Soy del tipo supervisor")
    
    def imprimir_supervisor(self):
        super().imprimir_datos()
        print(f"Zona: {self.zona}")

    def __str__(self):
        return super().__str__() + f'\nZona: {self.zona}'

class Cliente(Persona):
    def __init__(self, nombre, apellidos, cedula, descuento):
        super().__init__(nombre, apellidos, cedula)
        self.descuento = descuento
    
    def get_tipo(self):
        print("Soy del tipo cliente")

    def imprimir_cliente(self):
        super().imprimir_datos()
        print(f"Descuento {self.descuento}")
    
    def __str__(self):
        return super().__str__() + f'\nDescuento {self.descuento}'