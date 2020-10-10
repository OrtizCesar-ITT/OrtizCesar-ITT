#Encontrar la suma de X numero de enteros (35)
init = 0
suma = 0
fin = int(input("Introduce hasta que numero vas a sumar:"))
for i in range(0,fin+1):
	suma = init + i;
	print(("%d + %d = %d") % (init,i,suma))
	init = suma

