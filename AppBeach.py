from paquetes.clases import Jugador,Torneo
from paquetes.funciones import sumaruno

contjug=1
conttor=1
jugadores=[]
torneos=[]
opcion=0
print("Bienvenido al sistema de Beach Volley Marplatense")
print("------------------------------------------------------------------------------")
while opcion !=9:
	print("\n1: Crear Jugador Nuevo\n2: Ver lista de Jugadores\n3: Crear torneo nuevo\n4: Ver lista de Torneos\n9: Salir")
	opcion=int(input("\nElija su opcion: "))

	if opcion == 1:
		A=Jugador(contjug)
		A.cargardatos()
		contjug=sumaruno(contjug)
		jugadores.append(A)
	else:
		if opcion == 2:
			print("Lista de Jugadores\n--------------------------------------------------------")
			for x in jugadores:
				print(x.nombre)
		else:
			if opcion == 3:
				A=Torneo(conttor)
				A.cargardatos()
				conttor=sumaruno(conttor)
				torneos.append(A)
			else:
				if opcion ==4:
					print("Lista de Torneos\n--------------------------------------------------------")
					for x in torneos:
						print(x.nombre)





