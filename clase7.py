#6. Funciones
def suma(a,b):
    resultado = a + b
    return resultado

def saludar(message):
    print(message)


def mostrar_edad(message, edad=18):
    resultado_edad = message + str(edad)
    return resultado_edad


resultado_funcion = suma(1,2)

saludar(2)
resultado_edad = mostrar_edad("tu edad es ")
print(resultado_edad)
