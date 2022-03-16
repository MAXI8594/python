
dato1 =int(input("ingrese un numero: "))
dato2 = int(input("ingrese otro numero: "))



if dato1 %2 == 0 and dato2%2==0:
    print("ambo numero son par")
elif dato1 %2 == 0 and dato2 %2 != 0 :
    print(f"{dato1} es par")
    print(f"{dato2} es impar")
elif dato1 %2 != 0 and dato2 %2== 0 :
    print(f"{dato2} es par")
    print(f"{dato1} es impar")
elif dato1 %2 != 0 and dato2 %2 != 0 :
    print(f"{dato2} es impar")
    print(f"{dato1} es impar")

