def desvocalizador(word): # Función requiere recibir una palabra
    vocales = "aeiou" # Variable que maneja las vocales
    for i in vocales: # Bucle for itera con cada vocal
        word = word.replace(i, "") # Con cada iteración de vocal, esta es reemplazada por un espacio vacío
    print(word) # Print para comprobar resultado
    for i in enumerate(word): # Enumerate() enumera y declara las letras sobrantes en pares de tuplas
        print(i) # Resultado final

desvocalizador("paralelepipedo")