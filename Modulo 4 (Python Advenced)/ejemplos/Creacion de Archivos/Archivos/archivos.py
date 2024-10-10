from io import open

def crear_archivo():
    try:
        archivo = open('datos.csv', 'x')
        archivo.close()
    except FileExistsError:
        print("El archivo datos.cvs existe o a sido creado previamente")
    except Exception as error: 
        print('Se ha generado un error no previsto', type(error).__name__)

crear_archivo()