class Vehiculo:
    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self. cilindrada = cilindrada
    def cadena(self):
        return f'Marca {self.marca}, Modelo {self.modelo}, {self.n_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc'




###Código para instanciamiento dinámico###
n_vehiculos = int(input('Cuantos vehículos desea insertar: ')) #variable que controla número de iteraciones
instancias = [] #lista que guarda las instancias
for vehiculo in range(n_vehiculos):
    print('--------------------')
    print(f'Datos del automóvil {vehiculo + 1}') #numero de automovil
    marca = input('Inserte la marca del automóvil: ') #Formulario de inputs
    modelo = input('Inserte el modelo: ')
    n_ruedas = input('Inserte el número de ruedas: ')
    velocidad = input('Inserte la velocidad en Km/h: ')
    cilindrada = input('Inserte el cilindraje en CC: ')
    variable = f"automovil_{vehiculo}" #variable que almacenará el nombre de las claves de instancia "automovil_n"
    instancias.append (Automovil(marca, modelo, n_ruedas, velocidad, cilindrada)) #se asigna como valor una instancia especifica 

contador = 1
for instancia in instancias:
    print(f"\nDatos del automovil {contador}:", instancia.cadena())
    contador += 1