#Determinar el segundo numero entero mas grande de un conjunto de quince enteros suministrados
mayor = 0
seg = 0
numbs = [float(input("Inserte Numero a comparar:")) for x in range (5)]

for t in numbs:
	if (t > mayor):
		seg = mayor
		mayor = t

		if (t > seg and t!= mayor):
			seg = t

			
print(numbs)
print("El segundo numero mayor es: " + str(seg))
