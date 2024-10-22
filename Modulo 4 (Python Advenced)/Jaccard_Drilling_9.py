def word_replacer(old_word, new_word):
    try:
        with open('informacion.dat', 'r') as archivo:
            lineas_reemplazo = []
            for linea in archivo:
                linea = linea.strip()
                cambios = linea.replace(old_word, new_word)
                lineas_reemplazo.append(cambios)
        reemplazo = '\n'.join(lineas_reemplazo)
        with open('informacion.dat', 'w') as archivo:
            archivo.write(reemplazo)
    except FileNotFoundError:
        print('No se encuentra el archivo informacion.dat. Por favor, ejecute "Jaccard_Drilling_8.py" para generar el archivo.')
    except Exception as error:
        print('Se ha generado un error imprevisto', type(error).__name__)
    finally:
        print('Contenido reemplazado correctamente. ')
    
word_replacer('informacion', 'Procesamiento') #archivos con extensión .dat no soportan tildes, así que es importante asegurarse de que el texto sea escrito sin tildes.