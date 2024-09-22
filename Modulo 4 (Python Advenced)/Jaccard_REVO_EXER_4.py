class Libro:
    def __init__(self, autor, titulo, anio = None):
        self.autor = autor
        self.titulo = titulo
        if anio is not None:
            self.anio = anio


libro_1 = Libro("Dan Brown", "Inferno")
libro_2 = Libro("Dan Brown", "El Código Da Vinci", 2003)

print(libro_1.__dict__)
print(libro_2.__dict__)