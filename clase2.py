#2. Variables y operadores 

print("Hola mundo")
# variables
# variable de tipo string ( texto )
nombre_usuario = "Chanchito"

# variable de tipo entero (numero entero)
ejemplo_numero = 45

# variable de tipo decimal (float)
numero_flotante  = 4.56

# variable de tipo booleano ( bool )

valor_booleano  =True
valor_booleano_2 = False

# variables que almacenan estructuras de datos

listas = list()

# diccionarios
diccionario  = dict()

# saber el tipo de dato de las variables

print(type(nombre_usuario))
print(type(ejemplo_numero))
print(type(numero_flotante))
print(type(valor_booleano))
print(type(valor_booleano_2))
print(type(listas))
print(type(diccionario))

# operadores aritmeticos

suma = 1 + 2
resta = 4 - 10
multiplicacion =  4 * 10
potenciacion = 2 ** 4
division =  4/2
modulo =  10%2

print(suma)
print(resta)
print(multiplicacion)
print(potenciacion)
print(division)
print(modulo)

#trasnformar tipos de variables

numero_texto = "234"
resultado = int(numero_texto)   + 5.5
print("el resultado de la operacion es: " + str(resultado))

edad_usuario = 22

print("LA EDAD DEL USUARIO ES : " + str(edad_usuario))


entrada_nombre_usuario = input("POR FAVOR INGRESA TU NOMBRE: ")
entrada_edad_usuario = int(input("POR FAVOR INGRESA TU EDAD: "))

mensaje_final = "Bienvenido usuario "+ entrada_nombre_usuario + " tu edad es " + str(entrada_edad_usuario)
print(mensaje_final)