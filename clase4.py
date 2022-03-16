# 4. Listas, Iterables y Ciclos
#link de la plataforma https://www.hackerrank.com/
#formas de declarar listas
lista_objetos = [1,2,3,"latinoamerica",[40,45,50,[1,2,3]], True]
lista_vacia = []
lista = list()

# accediendo a los elementos de una lista
print(lista_objetos[3]) #imprime latinoamerica de la lista_objetos
print (lista_objetos[4][3][1])


#agregar elementos a lista de objetos
print("ESTA ES LA LISTA DE OBJETOS INICIAL" , lista_objetos )
lista_objetos.append("PROGRAMAR ES GENIAL")
print(lista_objetos)
#eliminar "latinoamerica" de la lista de objetos
lista_objetos.pop(3)
lista_objetos.pop()
print(lista_objetos)
#ordenar lista de numeros

lista_numeros = [ 10,25,-1,-2]
lista_numeros = sorted(lista_numeros)
print(lista_numeros)

#recorrer lista
lista_usuarios = ["carlos","andres","juan"]
tamano_lista = len(lista_usuarios)
for usuario in lista_usuarios:
    if usuario == "carlos":
        print("ESTE USUARIO TIENE MULTAS")
    elif usuario == "andres":
        print("ESTE USUARIO ESTA DEBIENDO SOLO 50000 PESOS")
    elif usuario == "juan":
        print("ESTE USUARIO NO TIENE DEUDAS")
    
for contador in range(10):
    print("HOLA MUNDO")


print("ESTE ES EL TAMAÑO DE LA LISTA:"+ str(tamano_lista))

for contador in range(len(lista_usuarios)):
    print( lista_usuarios[contador])




