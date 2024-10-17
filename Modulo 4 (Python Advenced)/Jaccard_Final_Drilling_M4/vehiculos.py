import csv

class Vehiculo:
    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def guardar_datos_csv(self): #Método que guarda la información en un archivo CSV
        try:
            with open("vehiculos.csv", "a", newline= '') as archivo: #Exporta los elementos de la lista a vehiculos.csv
                archivo_csv = csv.writer(archivo)
                datos = [(self.__class__, self.__dict__)] #La clase se autoreferencia a sí misma para que los resultados se adapten a las caracteristicas de cada clase heredada
                archivo_csv.writerows(datos)
        except Exception as error:
            print('Se ha generado un error imprevisto', type(error).__name__)
        
    def leer_datos_csv(self, i): #El método toma la variable 'i' (enviado desde main) para considerar la posición en la lista de cada instancia
        try:
            with open("vehiculos.csv", "r") as archivo:
                archivo_csv = csv.reader(archivo)
                filas = list(archivo_csv) #Convierte el archivo en una lista iterable para poder acceder a su información desde los índices
                print('Lista de Vehículos', self.__class__.__name__)
                print(filas[i], '\n') #Imprime las filas en base a los índices.
        except FileNotFoundError:
            print('No se encuentra el archivo vehiculos.csv. Por favor, creelo o verifique la ruta en la que se encuentra.')
        except IndexError:
            print('Existe un error en los índices del archivo vehiculos.csv. Por favor, vuelva a guardar los datos.')
        except Exception as error:
            print('Se ha generado un error imprevisto', type(error).__name__)
        
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