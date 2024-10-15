def agregar_datos_archivo():
    try:
        archivo = open('datos.csv', 'a')
        archivo.write('\nlinea 6 agregada')
        archivo.close()
        print('listo')
    except FileNotFoundError:
        print('No se encuentra el archivo datos.csv')
    except Exception as error:
        print('Se ha generado un error imprevisto', type(error).__name__)

agregar_datos_archivo()