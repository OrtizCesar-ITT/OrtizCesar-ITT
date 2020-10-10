#Suma los numeros enteros del 1 al 1000
init = 0
suma = 0
for i in range(0,1001):
	suma = init + i;
	print(("%d + %d = %d") % (init,i,suma))
	init = suma