#Encontrar el entero positivo mayor en una lista de quince enteros, algunos de los cuales son impares
import random
mayor = 0;
#Ingreso de valores
lista = []
for x in range(15):
	x = random.randint(1,100)
	lista.append(x)
print(lista)

for y in lista:
	if (y > mayor):
		mayor = y
	else:
		mayor = mayor

print("El numero mayor de la lista es: " + str(mayor))
