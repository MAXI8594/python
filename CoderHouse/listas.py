#Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

#Añade a la LISTA1 el int 1234 y luego el string “Hola”
#Añade a la LISTA2 el string “Adios” y luego el int 1234
#Genera una LISTA3 con todos los elementos de la LISTA1 menos el último
#Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último
#Genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3#


lista_1= [1,12,123]
lista_2= ["Bye","Ciao","Agur","Adieu"]

#
lista_1.append(1234)
print(lista_1)

#
lista_2+=('Adios',1234)
print(lista_2)

#
lista3= lista_1[0:2]
print(lista3)
#
lista4= lista_2[1:3]
print(lista4)
#
lista5 = lista4 +lista3
print(lista5)


tupla = (5, 12, 7, 37, 8, 86, 19, 7, -783, 87, 188, 7, 9, 12, 7, 3982)