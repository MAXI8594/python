
n1=int(input("ingrese el primer numero: "))
n2=int(input("ingrese el segundo numero: "))
n3=int(input("ingrese el tercer numero: "))

if n1>=n2 and n1>=n3:
    print(f"el numero {n1} es el mayor de los tres")
elif n2>=n1 and n2>=n3:
    print(f"el numero {n2} es el mayor de los tres")
elif n3>=n1 and n3>=n2:
    print(f"el numero {n3} es el mayor de los tres")
