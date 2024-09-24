class A:
    def __init__(self):
        print("Pertenezco a la clase A")

    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")

    def metodo_b(self):
        print("Método heredado de B")

class C(B, A):
    def __init__(self):
        super().__init__()

    def metodo_c(self):
        print("Método de clase C")

c = C()

c.metodo_a()
c.metodo_b()
c.metodo_c()