class Pokemon:

    animal = "pikachu"

    def __init__(self, poder,edad, color):
        self.poder = poder
        self.edad = edad
        self.color = color
    
    def saludar(self):
        print("picka picka...")
    
    def mostrar_edad(self):
        print(f"mi edad es...{self.edad}")
    
    def restar_edad(self):
        if self.edad >= 40:
           self.edad -= 2
        print(f"mi nueva edad es {self.edad}")



pokemon_1 = Pokemon("rayos de electricidad", 43, "rojo")
pokemon_2 = Pokemon("electromagnetismo",40,"amarillo")
pokemon_1.saludar()
pokemon_1.mostrar_edad()
pokemon_2.mostrar_edad()

pokemon_1.restar_edad()
pokemon_2.restar_edad()





