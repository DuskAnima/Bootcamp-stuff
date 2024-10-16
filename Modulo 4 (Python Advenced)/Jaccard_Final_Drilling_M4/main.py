from vehiculos import Vehiculo, Automovil, Bicicleta, Carga, Particular, Motocicleta
import csv

def instanciamiento_dinamico():
    n_vehiculos = int(input('Cuantos vehículos desea insertar: ')) #variable que controla número de iteraciones
    instancias = [] #lista que guarda las instancias
    for vehiculo in range(n_vehiculos):
        print('--------------------')
        print(f'Datos del automóvil {vehiculo + 1}')
        marca = input('Inserte la marca del automóvil: ') #Formularios de inputs que controlan variables de instancia
        modelo = input('Inserte el modelo: ')
        n_ruedas = input('Inserte el número de ruedas: ')
        velocidad = input('Inserte la velocidad en Km/h: ')
        cilindrada = input('Inserte el cilindraje en CC: ')
        instancias.append (Automovil(marca, modelo, n_ruedas, velocidad, cilindrada)) #se acomplan las variables y se añade la respectiva instancia a la lista

    for i, instancia in enumerate(instancias): #Se accede a las instancias desde su respectivo numero de lista
        print(f"\nDatos del automovil {i + 1}:", instancia.cadena()) #Se llama al método que guarda la información concatenada

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

particular.guardar()
carga.guardar()
bicicleta.guardar()
motocicleta.guardar()

"""

print(particular.cadena())
print(carga.cadena())
print(bicicleta.cadena())
print(motocicleta.cadena())

print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automóvil:", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo Particular:", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))

"""

def guardar(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "w")
    datos = [(Automovil.__class__, Automovil.__dict__)]
    archivo_csv = csv.writer(archivo)
    archivo_csv.writerows(datos)
    archivo.close()
def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
        archivo.close()
        return vehiculos
    

