def reemplazar_datos_archivo(texto_viejo, texto_nuevo):

    try:
        archivo = open('datos.csv', 'r')
        reemplazo = ""
        for linea in archivo:
            linea = linea.strip()
            cambios = linea.replace(texto_viejo, texto_nuevo)
            reemplazo = reemplazo + cambios + "\n"
        archivo.close()

        archivo_reemplazo = open('datos.csv', 'w')
        archivo_reemplazo.write(reemplazo)
        archivo_reemplazo.close()
    except FileNotFoundError:
        print("No se encuentra el archivo datos.csv")
    except Exception as error:
        print("se ha generado un error no previsto", type(error).__name__)
    finally:
        print("Se ha reemplazado satisfactoriamente")

reemplazar_datos_archivo("linea", "LINEA")
