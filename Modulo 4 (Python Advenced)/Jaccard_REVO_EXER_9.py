def aggregator_stuff():
    try:
        with open('informacion.dat', 'r+') as archivo:
            contenido = archivo.read() #Asignar el archivo a una variable con .read() evita la sobreescritura porque mueve el puntero al final.
            if contenido:
                archivo.write('Hola Mundo\nEste en una nueva línea en el archivo\nagregando la segunda línea del archivo\nfinalizando la linea agregada')
                #En este caso no hubo necesidad de agregar una linea nueva al principio porque el archivo informacion.dat posee el salto de linea.
    except FileNotFoundError:
        print('No se encuentra el archivo informacion.dat. Por favor, ejecute "Jaccard_Drilling_8.py" para generar el archivo.') 
        #En caso de que no exista el archivo, ejecutar "Jaccard_Drilling_8"
    except Exception as error:
        print('Se ha generado un error imprevisto', type(error).__name__)
    
aggregator_stuff()