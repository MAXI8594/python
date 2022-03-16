<<<<<<< HEAD
class calculo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return str(self.base * self.altura)

base = int(input("proporcione la base : "))
altura = int(input("proporcione la altura : "))
rectangulo = calculo(base, altura)

=======
class calculo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return str(self.base * self.altura)

base = int(input("proporcione la base : "))
altura = int(input("proporcione la altura : "))
rectangulo = calculo(base, altura)

>>>>>>> 8bff4719af79005fd02c67d85b7b76d9f0784eda
print("el area es", rectangulo)