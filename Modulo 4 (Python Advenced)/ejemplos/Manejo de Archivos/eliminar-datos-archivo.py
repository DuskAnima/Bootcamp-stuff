def eliminar_datos_archivo():
    try:
        archivo = open('datos.csv', 'w')
        archivo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.csv')
    except Exception as error:
        print('Se ha generado un error imprevisto', type(error).__name__)
    finally:
        print('Se han eliminado todos los datos del archivo exitosamente')

eliminar_datos_archivo()
