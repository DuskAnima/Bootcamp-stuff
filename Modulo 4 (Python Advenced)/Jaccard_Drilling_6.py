import time

usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}
id_usuario = '004'

try:
    print(usuarios[id_usuario])
except KeyError:
    print('La clave 004 no está en el diccionario. Añadiendo clave...')
    usuarios[id_usuario] = 'Ninguno'
    time.sleep(1)
    print("---------------")
    print(usuarios)