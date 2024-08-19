def numberAnalizer(n):
    if n == 0:
        print("Cero")
    else: 
        if n > 0:
            print("Positivo")
        else:
            print("Negativo")
        if n % 2 == 0:
            print("Par")
        else:
            print("Impar")

numberAnalizer(0)