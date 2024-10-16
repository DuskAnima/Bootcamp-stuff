import csv

class Vehiculo:
    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def guardar(self):
        with open("vehiculos.csv", "a") as archivo:
            archivo_csv = csv.writer(archivo)
            datos = [(self.__class__, self.__dict__)]
            archivo_csv.writerows(datos)

    def 

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self. cilindrada = cilindrada

    def cadena(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc'

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, tipo):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo = tipo

    def cadena(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas}, Tipo: {self.tipo}'

class Carga(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, capacidad):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.capacidad = capacidad

    def cadena(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc, Carga {self.capacidad} Kg'


class Particular(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, n_asientos):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.n_asientos = n_asientos

    def cadena(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc, Puestos: {self.n_asientos}'

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, n_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, n_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def cadena(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas}, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}'