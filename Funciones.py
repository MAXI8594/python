import re


def mult (a,b):
    print("se esta ejecutando")
    c = a*b
    return c


def comparar (n1,n2):
    if n1 > n2 :
        print("el primer valor es mayor")
    elif n2 > n1 :
        print("el segundo es mayor")
    else:
        print("son iguales ")



if __name__=='__main__':
    res = mult (7,7)
    print(res)
    comparar(2,5)


