def factorial (n):
    f = 1
    for i in range(n):
        f *= i+1
    print(f"el factorial de {n} es {f}")

factorial(5)




# > n = total de iteraciones.
# > i = valor de cada iteración.
# > i es el numero de iteraciones y estas comienzan en 0. Para operar con enteros se debe sumar 1 
# para que la secuencia sea desde 1 hasta n.
# > las iteraciones tendrían que ser:  
# 1*i(1) = 1. Reservo 1. 1*i(2) = 2. Reservo 2. 2*i(3) = 6. Reservo 6. 6*i(4) = 24. Reservo 24. 24*i(5) = 120
# > Para reservar es necesaria una variable que se auto actualice. Será f = 1, debido a que 1 es 
# un elemento neutro
# > Para reservar el resultado, el primer valor del factor debe estar determinado afuera del bucle