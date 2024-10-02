
def edad_struff():
    while True:
        edad = input("Ingrese su edad: ")
        try:
            if int(edad) >= 18:
                print("Usted es adulto")
                break
            else:
                print("Usted no es adulto")
                break
        except ValueError:
            print("Ingrese su edad nuevamente")


edad_struff()