#Suma los numeros del 1 al 20
init = 0
suma = 0
for i in range(0,21):
	suma = init + i;
	print(("%d + %d = %d") % (init,i,suma))
	init = suma