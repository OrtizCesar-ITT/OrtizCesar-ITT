#Imprimir la tabla de sumar hasta 12+12
print("Tabla de sumar de 1 a 12")
numero = int (input("Introduce numero a sumar: "))
for i in range(0,13):
	res = i+numero
	print(("%d + %d = %d")%(numero, i, res))