#Consigna: Crear un programa para calcular la nota final del estudiante en base a dos exámenes, 
# los exámenes cuentan con un porcentaje distinto de la nota final

nombre=input("Ingrese su nombre:  ")
nota1= float(input(("Ingrese la nota del primer examen: ")))
nota2= float(input(("Ingrese la nota del segundo examen: ")))

print(f"La nota final de {nombre} es {(nota1*0.4) +(nota2*0.6)}")