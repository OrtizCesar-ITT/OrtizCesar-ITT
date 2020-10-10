#Suma de numeros pares del 2 al 2000
suma = 0

for i in range(0, 2001):
	if i%2==0:
		suma+=i

print("La suma es: ", suma)