
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3=[]

for i in lista_1:
        if i in lista_2 and i not in lista_3:
            lista_3.append(i)
print(lista_3)



n1=int(input("Ingrese en primer numero >>  "))
n2=int(input("Ingrese en segundo numero >>  "))
print("-"*50)
print("[1]Suma entre dos numeros")
print("[2]Resta entre dos numeros")
print("[3]Producto entre dos numeros")

print("-"*50)
op = int(input("Elija una opcion >>  "))
print("-"*50)
if op ==1:
    print(f"El resultado de la suma es >> {n1+n2}")
elif op ==2:
    print(f"El resultado de la resta es >> {n1-n2}")
elif op ==3:
    print(f"El resultado del producto es >> {n1*n2}")
else:
    print("Opcion incorrecta")



n=0
while n % 2 == 0:
    n = int(input("Ingrese un numero impar >>  "))


total=0

for i in range(0,101,1):
    if i %2 != 0:
        total += i
print(f"La sumatoria de los las numero impares de 0 a 100 es  {total}")

suma=0
n = int(input("Ingrese la cantidad de numeros con los que quiere operar: "))
for i in range(n):
    
    suma += (int(input("Intruduzca un numeros>> ")))
print(f"La media entre los numero que ingresaste es de >> {suma/n}")

lista=[]
n=0
while True:
    n = int(input("Ingrese un numero entre el 0 y el 9 >> "))
    if n >=0 and n<=9:
        lista = lista.append(n)
        break
print(lista)

    
lista = []
n = int(input("Ingrese ingrese la cantidad de numeros que quiere poner en una lista  >> "))
for i in range(n):
    l=int(input("Ingrese un numero entre el 0 y 9 para generar una lista >> "))
    lista.append(l)
print(lista)

while True:
    b = int(input("Ingrese un numero entre 0 y 9 >> "))
    if b >=0 and b <= 9:
        break
if b in lista:
    print("El numero ingresado se encuentra dentro de la lista ")
else:
    print("El número ingresado no se encuentra en la lista")

print(list(range(11)))
print(list(range(-10, 1)))
print(list(range(0, 21, 2)))
print(list(range(-19, 0, 2)))
print(list(range(0, 51, 5)))