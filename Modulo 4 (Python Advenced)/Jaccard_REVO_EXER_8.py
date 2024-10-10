from io import open

def data_creator():
    try:
        with open('informacion.dat', 'x') as data:
            for i in range(5):
                data.write(f'Datos de información en la línea {i+1}.\n')
    except FileExistsError as error:
        print (f"{type(error).__name__}: EL archivo que está intentando crear ya existe.")


data_creator()