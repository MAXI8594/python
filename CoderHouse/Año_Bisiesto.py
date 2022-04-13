
#desde1582


def bisiesto(año):
    if año %4==0 and año%100!=0:
        resp=print(">> Este año es biciesto")
        return resp
    elif año%100==0 and año%400==0:
        resp=print(">> Este año es biciesto")
        return resp
    else:
        resp=print(">> Este año no es biciesto")
        return resp
año = int(input("Ingrese un año a partir de 1582 >>  "))

bisiesto(año)