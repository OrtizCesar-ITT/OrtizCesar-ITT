#Introducir de 25 numeros y determinar la cantidad de positivos y negativos del conjunto
ctPos = 0
ctNeg = 0
numbs = [float(input("Inserte Numero a comparar:")) for x in range (25)]
for t in numbs:
	if (t < 0):
		ctNeg += 1
	else:
		ctPos += 1

print("La cantidad de numeros positivos: " + str(ctPos) )
print("La Cantidad de numeros negativos: " + str(ctNeg) )
print(numbs) 