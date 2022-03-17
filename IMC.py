#Indice de Masa Corporal
import math
from re import I

a = float(input("Ingrese su altura: "))
m = float(input("Ingrese su peso: "))
ind= m/(a**2)
    

print(f"El Indice de masa corporal es de : {ind:.1f} ")

if ind < 18.5:
        print("Bajo peso")
elif ind == 18.5 or ind < 24.9:
        print("Normopeso")
elif ind == 25 or ind < 29.9:
        print("Sobreso")
elif ind == 30 or ind < 34.9:
        print("Obesidad I")
elif ind == 35 or ind < 39.9:
        print("Obesidad II")
elif ind >= 40:
        print("Obesidad Morbida")
elif ind >= 50:
        print("Obesidad IV")
elif ind >= 60:
        print("Obesidad V")
else: print("Los datos ingresados son incorresctos")








