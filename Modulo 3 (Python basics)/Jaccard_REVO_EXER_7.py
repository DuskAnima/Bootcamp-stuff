def numberAnalizer(numbers):
    for n in numbers:
        if n == 0:
            print(f"{n} es Cero")
        else: 
            if n % 2 == 0:
                print(f"{n} es Par")
            else:
                print(f"{n} es Impar")

numbers = 2,3,2,6,8,0,1

numberAnalizer(numbers)