def areaTriangulo(b, h):
    if b > 0 and h > 0:
        return print(b * h)
    else:
        print("Ingrese solo números positivos")
    

b = int(input("ingrese base:"))
h = int(input("ingrese altura:"))
areaTriangulo(b, h)