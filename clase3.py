valor_booleano  =False

edad = 50

mayor_edad =  edad >= 18 and edad <35

operador_or = edad >= 18 or edad <35

print(mayor_edad)
print(operador_or)

numero1 = 25
numero2 = 2.56
numero3= 0
numero4 = 1
print(bool(numero1))
print(bool(numero2))
print(bool(numero3))
print(bool(numero4))

nueva_edad = 25

if(nueva_edad > 18):
    print("LA PERSONA ES MAYOR DE DEDAD")
    print("LA CONDICION SE CUMPLIO")
    if nueva_edad > 30:
        print("LA PERSONA SE ESTA ACERCANDO A LOS 40")
    else:
        print("LA PERSONA AUN ES JOVEN")
elif (nueva_edad > 15):
    print("NO ES MAYOR DE EDAD PERO YA ES ADOLESCENTE")

else:
    print("LA PERSONA ES MENOR DE EDAD")

print("HOLAAAA YA SALI DE LOS IF")



