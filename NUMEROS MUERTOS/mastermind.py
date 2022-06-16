"""
	Este juego trata de adivinar los 4 numeros y su orden que el ordenador ha generado en 15 intentos

	VARIABLES DE INICIO

		- digitos = Esta para ser comparada con el numero introducido y ver que haya introducido solo numeros
		- numero = Numero que el jugador debe adivinar (se escage al azar)
		- Muertos = Numero que contabliza si ha acertado el numero y la posicion (se reinicia cada ronda)
		- Heridos = Numero que contabliza si ha acertado el numero (se reinicia cada ronda)
		- intento = Numero introducedi por el jugador cada ronda para probar si ha ganado
		- intentos = Lista con los numeros, muertos y heridos de cada ronda
		- salir = Variable que permite cerrar la ejecucion del programa

	FLUJO DEL PROGRAMA

		Aparece la pantalla de inicio de la aplicacion, al presionar enter empieza el juego

		- Se elige al azar el numero que se tiene que adivinar
		
		CICLO
		- Se muestra la tabla con los intentos realizados 
		- Se comprueba si se ha ganado
		- Se comprueba si quedan intentos
		- Se pide el numero
		- Se comprueba si quiere salir
		- Se comprueba si hay heridos o muertos
		- Añadimos resultados a la lista de intentos
		- Se reinician las variables de muertos y heridos para la siguiente ronda

"""
import random,os

digitos="0123456789" # Digitos posibles
numero= "" # Numero que hay que adivinar
muertos=0 
heridos=0
intento=None # Ultimo numero elegido
intentos = [] # Guarda el numero que ha dicho y el resultado de intentos y heridos
salir = False


os.system('cls')


print('''

	*********************************
	*                               *
	*           MASTERMIND          *
	*                               *
	*     TIENES SOLO 15 INTENTOS   *
	*                               *
	*********************************

	''')

input(" 	Pulsa enter para comenzar...")

# Se elige el numero y se comprueba que cada digito sea diferente
while len(numero) < 4:
	digito = random.choice(digitos)
	if digito not in numero:
		numero+=digito


# EMPIEZA EL JUEGO-------------------------------------------------------
while True:

	os.system('cls')

	print(''' 
		
			+--------------------------------------------------------------+
			|                                                              |
			|                     MUERTOS Y HERIDOS                        |
			|                                                              |
			|                     "exit para salir"                        |
			|                                                              |
			+--------------------------------------------------------------+
			|                                                              |
			|               NUMERO        |          M  -  H               |''')

	# Imprimimos la lista con los intentos
	for i in range(len(intentos)):
		print(" 			|______________________________________________________________|")
		print(" 			|                                                              |")
		print(" 		{}º	|               {}          |          {}  -  {}               |".format(intentos[i][3], intentos[i][0], intentos[i][1], intentos[i][2]))





	# Comprobamos si ha ganado
	if intento==numero:
		print(" 			|______________________________________________________________|")
		print("\n\n			HAS GANADO!!!")
		print()
		print(" 			---------------------------------")
		print()
		print(" 				Intentos: "+str(len(intentos)))
		break





	# Comprobamos si le quedan intentos
	if len(intentos)>=15:
		print(" 			|______________________________________________________________|")
		print("\n\n 				HAS PERDIDO, TE HAS QUEDADO SIN INTENTOS")




	# PREGUNTAMOS EL NUMERO
	# Comprobamos que el numero es valido
	valido = False
	while not valido:
		valido = True
		intento = input("\n 			Introduce que numero => ")
		if intento == "exit":
			salir = True
			break
		if len(intento) != 4:
			valido = False
			print(" 			*Introduce cuatro digitos*") 
		for i in intento:
			if i not in digitos:
				valido = False
				print(" 			*Solo numeros del 0-9*")
				break

		pos = 0
		# Comprobamos que no hay dos nº iguales, el pos es para que al comprobar una posicion comience desde la siguiente y no se comprueba a si mismo
		# El -1 es pq el ultimo no tiene que comprobar nada pq ya ha sido comprobado por los otros
		for i in intento[:-1]:
			pos+=1
			if i in intento[pos:]:
				valido = False
				print(" 			*No se pueden repetir numeros*")
				break

		




	# Comprobamos si ha elegido salir
	if salir==True:
		print(" 			La solucion era "+ numero)
		break




	# Comprobamos si hay muertos o heridos

	for i in range(4):
		if intento[i] in numero:
			if intento[i]==numero[i]:
				muertos+=1
			else:
				heridos+=1


	# Añadimos los datos del intento a la lista
	intentos.append([intento, muertos, heridos, len(intentos)+1])


	# Reiniciamos las variables
	muertos=0
	heridos=0



	