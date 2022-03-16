class calculo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return str(self.base * self.altura)

base = int(input("proporcione la base : "))
altura = int(input("proporcione la altura : "))
rectangulo = calculo(base, altura)

print("el area es", rectangulo)