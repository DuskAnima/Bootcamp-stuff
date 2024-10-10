from io import open

def lectura_archivo():
    try:
        archivo = open('datos.csv', 'r')
        contenido = archivo.read()
        archivo.close()
        print(contenido)
    except FileNotFoundError:
        print("No se encuentra el archivo datos.cvs")
    except Exception as error:
        print("se ha generado un error no previsto", type(error).__name__)

lectura_archivo()