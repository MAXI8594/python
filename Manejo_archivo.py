nombre = input("Ingrese el nombre que se alamcenara\n>>")
file = open("nombres.txt","a")
file.write(nombre+"\n")
file.close()