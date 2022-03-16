#bucle While
from ast import While
import math

n = int(input("escribe un numero : "))
while n<0:
    print("ingrese un numero positivo")
    n = int(input("vuelva a escribe un numero : "))
print(f"El resultado de las raiz cuadrada es: {math.sqrt(n)}")