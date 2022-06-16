'''  JUEGO 3 EN RAYA   '''

# Importamos las librerias
import random
import os
import time

# Selecciona el nivel de dificultad
def presentacion_1():

	"""LA FUNCION PRESENTACION UNO PREGUNTA AL USUARIO EL NIVEL DE DIFICULTAD
		*LA DIFICULTAD DIFICIL NO ESTA IMPLEMENTADA*"""

	print('''


					= TRES EN RAYA =


					1. FACIL
					2. DIFICIL



		''')
	# Al principo no hay nivel seleccionado por lo que el codigo entra en el bucle
	nivel = ""
	while nivel !=1 and nivel !=2:
		nivel = int(input(" 				-->  "))
	return int(nivel)




# El jugador elige que ficha jugar
def presentacion_2():

	"""Devuelve la ficha elegida por el jugador"""

	print('''


					- Elige tu ficha -

					Empieza la ficha "O"

					Elige: O/X
			
		''')

	ficha=""
	while ficha !="O" and ficha !="X":
		ficha = input(" 				-->  ").upper()

	# Dependiendo de que ficha escoja el jugador, se asignara la otra a la maquina

	if ficha=="O":

		humano="O"
		ordenador="X"

	else:
		humano="X"
		ordenador="O"

	# Retorna ambas variables
	return humano, ordenador



# Muestra el tablero
# Se pasa como parametro una lista con los valores de cada casilla
# Al llamar el tablero, este lo imprime segun los valores que tenga la lista
def mostrar_tablero(tablero):

	"""MUESTRA EL TABLERO DEL JUEGO"""


	print('''

	
						1       |2       |3 		
						   {}    |   {}    | {} 
						        |        |
						--------+--------+--------
						4       |5       |6 		
						   {}    |   {}    | {} 
						        |        |
						--------+--------+--------
						7       |8       |9 		
						   {}    |   {}    | {} 
						        |        |
						

		'''.format(tablero[0],tablero[1],tablero[2],tablero[3],tablero[4],tablero[5],tablero[6],tablero[7],tablero[8]))





# Cuando se termina la partida se pregunta si quiere seguir jugando
def seguir_jugando():

	"""PREGUNTA SI CONTINUARA LA PARTIDA"""

	print()
	respuesta = input(" 			Quieres seguir jugando [s/n] --> ").lower()
	if respuesta=="s":
		return True
	else:
		return False



# El algorimo comprueba si existe un 3 en raya
def hay_ganador(tablero, jugador):

	"""COMPRUEBA SI HAY 3 EN RAYA

		Se comprueba si el jugador pasado por marametros humano/ordenador
		tiene 3 en raya
	"""

	# La \ permite continuar en otra linea
	if tablero[0] == tablero[1] == tablero[2] == jugador or \
		tablero[3] == tablero[4] == tablero[5] == jugador or \
		tablero[6] == tablero[7] == tablero[8] == jugador or \
		tablero[0] == tablero[3] == tablero[6] == jugador or \
		tablero[1] == tablero[4] == tablero[7] == jugador or \
		tablero[2] == tablero[5] == tablero[8] == jugador or \
		tablero[0] == tablero[4] == tablero[8] == jugador or \
		tablero[2] == tablero[4] == tablero[6] == jugador:
		return True
	else:
		return False

# Comprueba si no quedan mas espacios en el tablero seleccionado
def tablero_lleno(tablero):
	""" El bucle recorre cada posicion de la lista en busca de valores vacios"""
	for i in tablero:
		if i == " ":
			return False
	else:
		return True

# Comprueba si la casilla esta libre
def casilla_libre(tablero, casilla):

	"""DEVUELVE SU UNA CASILLA ESTA LLENA O VACIA

		Se pasa como parametros el tablero donde se quiere comprobar y la casilla

	"""

	if tablero[casilla] ==" ":
		return True



# Esta funcion permita al jugador elegir la casilla que quiere marcar
def movimiento_jugador(tablero):

	"""DELVUELVE LA CASILLA ELEGIDA POR EL JUGADOR"""

	# Posiciones posibles
	posiciones = ["1","2","3","4","5","6","7","8","9"]
	# Posicion elegida por el jugador
	posicion = None

	# Se activa el bucle hasta un return o un break
	# El bucle se cierra cuando se ingrese una opcion correcta
	while True:

		# Si la posicion elegida no se encuentra entre la lista de opciones
		if posicion not in posiciones:
			# Se pregunta la casilla
			posicion = input(" 			Elige (1-9) --> ")
		# Si la opcion es valida
		else:
			# Se convierte a entero la opcion
			posicion = int(posicion)
			# Se comprueba si NO esta libre osea ocupada
			# Se pasa el parametro tablero 
			# Se pasa el parametro posicion elegida y se resta uno para que coincida con la lista de indices
			if not casilla_libre(tablero, posicion-1):
				print(" 			Posicion ocupada")
			# Si esta libre devuelve el indice correspondiente con la posicion
			else:
				return posicion-1

# Algoritmo de juego nivel facil
def mov_ordenador_facil(tablero, jugador):

	"""EL ORDENADOR SOLO INTENTARA NO SER GANADO

		El oredenado solo comprueba si en la siguiente jugada podria ser ganado y trata de evitarlo
		colocando la ficha donde comprueba que el jugador le ganaria

	"""

	# Crea ciclo que prueba en cada posicion si el jugador le ganaria si pusiera una ficha ahi
	for i in range(9):

		# Creamo una copia del tablero para no tocar el table de juego y asi poder probar
		# Para hacer una copia usamos list, sino solo estariamos asignando una variable
		# La copia al estar dentro del bucle se reinicia a su estado original con cada ciclo
		copia_tablero = list(tablero)
		# Comprueba si la casilla donde quiere probar esta libre
		if casilla_libre(copia_tablero, i):
			# Si esta libre asigna el valor del jugador ahi para comprobar que pasaria el jugador hace dicho movimiento
			copia_tablero[i] = jugador
			# Comprueba si le ganaria
			if hay_ganador(copia_tablero, jugador):
				# Si en esa posicion el jugador ganaria, el ordenador lo coloca ahi para bloquearle
				return i 

	# Si el ciclo anterior no funciona, y no retorna ningun resultado, el ordenador elige una posicion cualquiera
	while True:

		# Elige un numero del 0 al 8
		casilla = random.randint(0, 8)
		# Si esa casilla NO esta libre
		if not casilla_libre(tablero, casilla):
			# Vuelve a eligei un numero y al no haber mas codigo se reinicia el ciclo hasta ha
			casilla = random.randint(0, 8)
		# Si la casilla esta libre
		else:
			return casilla


def mov_ordenador_dificil(tablero, maquina, usuario):

	# Primero el oredenador comprueba si existe un movimiento que le permita ganar
	for i in range(9):
		copia = list(tablero)
		if casilla_libre(copia, i):
			copia[i]=maquina
			if hay_ganador(copia, maquina):
				return i

	# Luego comprueba que el usuario no pueda ganar
	for i in range(9):
		copia=list(tablero)
		if casilla_libre(copia, i):
			copia[i]=usuario
			if hay_ganador(copia, usuario):
				return i

	# Si la maquina sale segunda elegira el medio si esta libre
	if maquina == "X":
		# Si el medio esta libre
		if tablero[4] == " ":
			return 4
		# En caso contrario elegira una esquina
		else:
			# En cada turno comprueba cuales esquinas estan vacias para elegir una al azar
			vacias=[]
			for i in [0,2,6,8]:
				if tablero[i]==" ":
					vacias.append(i)
			# Elige una esquina de las vacias al azar si hay alguna libre
			if not len(vacias)==0:
				return random.choice(vacias)
	

	# Si empieza la maquina esta usara el primer movimiento al azar y el siguiente si puede al medio
	if maquina == "O":
		# Esto sirve para comprobar que turno es
		contador_vacias=0
		for i in tablero:
			if i == " ":
				contador_vacias+=1
		# Si hay 7 libres osea que han habido dos turnos 
		if contador_vacias==7:
			# Si la del medio esta libre
			if tablero[4]==" ":
				return 4

	# Si no se ha dado ninguna condicion anterior se escoge al azar
	while True:
		casilla = random.randint(0, 8)
		if casilla_libre(tablero, casilla):
			return casilla


################### INICIO DEL PROGRAMA ##################
# El programa se debe iniciar desde una consola para que funcionen las instruciones os.system

# Jugando es la variable el indica si el programa ha finalizado o no
jugando=True

while jugando:

	# Creamos el tablero, vacio, con 9 casillas del 0 al 8
	tablero = [" "]*9

	# Borra lo anterior 
	os.system('cls')

	# Pregunta el nivel de dificultad y lo almacena para elegir mas tarde que algoritmo usar
	nivel = presentacion_1()

	os.system('cls')

	# Preguntamos que ficha elegira y recivimos ambos valores del humano y ordenador
	humano, ordenador = presentacion_2()

	os.system('cls')

	# Mostramos el tablero de momento vacio
	mostrar_tablero(tablero)

	if humano == "O":
		turno = "Humano"
	else:
		turno = "Ordenador"


	# Este ciclo indica que la partida esta en curso
	partida=True

	while partida:

		# Como esta ciclo se recorre cada ronda lo priemor es comprobar aunque sea el primer ciclo si el tablero esta lleno
		if tablero_lleno(tablero):
			# Si esta lleno el resultado es tablas
			print(" 			EMPATE")
			# Se acaba la partida por lo tanto el ciclo
			partida = False



		# Si no esta lleno el tablero comprobamos a quien le toca

		# En esta caso si le toca al humano
		elif turno == "Humano":
			# Preguntamos que casilla escoge
			casilla = movimiento_jugador(tablero)
			# Se inserta el la lista el valor "X" o "O" segun que ficha haya escogido el jugador
			tablero[casilla] = humano
			# Se establece el turno al ordenador
			turno = "Ordenador"
			# Se limpia la patalla
			os.system('cls')
			# Se muesta el nuevo tablero actualizado
			mostrar_tablero(tablero)
			# Se comprueba si ha ganado el humano en su turno
			if hay_ganador(tablero, humano):
				print(" 			HAS GANADO")
				# Si ha ganado, el bucle se cierra
				partida = False

		# Si el turno es del ordenados
		elif turno == "Ordenador":
			# Hacemos que el ordenador se tome un tiempo para escribir
			print()
			print(" 		El ordenador esta pensando")
			# Se espera 2 segundos
			time.sleep(2)

			# Comprueba que nivel de dificulta hay escogido
			# En este caso solo hay uno
			if nivel == 1:
				# Devuelve la casilla que el ordenador ha elegido
				casilla = mov_ordenador_facil(tablero, humano)
			
			elif nivel == 2:
				casilla = mov_ordenador_dificil(tablero, ordenador, humano)
			# Aqui mas niveles....

			# Escribe en la lista su eleccion
			tablero[casilla] = ordenador
			# Pasa el turno al humano
			turno = "Humano"
			os.system('cls')
			mostrar_tablero(tablero)
			if hay_ganador(tablero, ordenador):
				print()
				print(" 			HAS PERDIDO")
				partida = False

	# Pregunta si quiere seguir jugando en caso negativo cierra el bucle
	# Asina el valor de la pregunta a la variable jugando que es la que mantiene el bucle
	jugando = seguir_jugando()