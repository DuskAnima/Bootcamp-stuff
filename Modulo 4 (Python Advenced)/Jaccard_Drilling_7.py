message = "Salario no está definido en el rango (1000 a 2000)"

class RangoSalarioError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


salario = int(input("Ingrese salario: "))
if salario < 1000 or salario > 2000:
    raise RangoSalarioError(message)
else:
    print("Salario ingresado exitosamente")

