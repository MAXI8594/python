from xml.etree.ElementTree import PI


import math
r = float(input("ingrese el valor del radio: "))

area = math.pi*r**2
log = 2*math.pi*r
print(f"El area del circulo es de : {area:.1f}")
print(f"La longitud del circulo es de : {log:.1f}")