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