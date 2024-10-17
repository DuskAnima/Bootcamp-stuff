from vehiculos import Vehiculo, Automovil, Bicicleta, Carga, Particular, Motocicleta

#Primer requerimiento: Generador dinámico de instancias de Automovil que devuelve los respectivos datos.
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

##########################################################################################################

#Instancias entregadas en el Segundo requerimiento
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

#Lista iterable de las instancias.
lista_vehiculos = [particular, carga, bicicleta, motocicleta]

#Resultados de segundo requerimiento. Se encuentran comentados para evitar que saturen la consola de información.
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

#funciones que llaman a los métodos solicitados en el tercer requerimiento.
def guardar_datos():
    with open("vehiculos.csv", "w"): #Linea de control que borra datos y se asegura de que la ejecusión reiterada no acumulará multiples veces la misma información
        for vehiculo in lista_vehiculos: #Metodo que itera la lista de instancias.
            vehiculo.guardar_datos_csv() #Accede al método que accede a los respectivos datos CSV

def leer_datos():
    for i, vehiculo in enumerate(lista_vehiculos):
        vehiculo.leer_datos_csv(i) #Variable vehiculo se encarga de llamar el método de la instancia mientras envía su respectiva posición en el índice
        
        #Cabe destacar que esta solución depende completamente de que la cantidad de índices en la base 
        # de datos(lista_vehiculos) y la cantidad de índices en el csv (vehiculos.csv) sea la misma
        # o generará errores.

guardar_datos()
leer_datos()