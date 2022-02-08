from modulos.operaciones import	Operaciones as op

print("""Qué deseas hacer?:
		1.-Sumar
		2.-Restar
		3.-multiplicar
		4.-Salir
		""")

opc = int(input("Elija una opción"))

objeto = op(2, 3)

if opc == 1:
	print(f"la suma es {objeto.suma()}")

elif opc == 2:
	print(f"la resta es {objeto.resta()}")

elif opc == 3:
	print(f"la multiplicación es {objeto.multiplicar()}")

else:
	print("Error")
	exit()