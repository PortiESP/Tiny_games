# BUSCA MINAS




import random, os


# -------------------------------------------------------------------------------------------PRESENTACION
def presentacion():

	"""IMPRIME LA PANTALLA DE INICIO Y LOS CONTROLES"""

	os.system('cls')
	print('''


		************************************
		*			BUSCAMINAS			*
		*								  *
		*	  w / a / s / d - moverse	 *
		*								  *
		*			m - mostrar		   *
		*								  *
		*	  b/v - marcar/desmarcar	  *
		*								  *
		*								  *
		************************************

		''')
	input(" 		Enter para comenzar...")






# -------------------------------------------------------------------------------------------MENU (movimiento)
def menu():

	"""PREGUNTA AL USUARIO QUE QUIERE HACER"""

	print()
	opcion = ""
	while opcion not in ["w", "a", "s", "d", "m", "b", "v"]:
		opcion = input(" 		¿w/a/s/d - m - b/v? ").lower()
	return opcion









# -------------------------------------------------------------------------------------------CREAR TABLERO
def crear_tablero(fil, col, val):

	"""CREA UNA MATRIZ CON LAS FILAS Y COLUMNAS Y EL VALOR QUE PASEMOS"""

	# Tablero almacena los valores para cada casilla
	# Creamos una matriz o tabla con las filas y columnas deseadas
	tablero = []
	for i in range(fil):
		tablero.append([])
		for j in range(col):
			tablero[i].append(val)
	return tablero


# -------------------------------------------------------------------------------------------MUESTRA EL TABLERO
def muestra_tablero(tablero):
	print("\n \n")

	"""MUESTRA EN FILAS Y COLUMNAS LA MATRIZ QUE PASEMOS"""

	# Imprime las filas 
	print(" 		", end="")
	print("* "*(len(tablero[0])+2))
	for fila in tablero:
		# Imprime al lado cada elemento de la fila
		print("		*", end=" ")
		for elem in fila:
			print(elem, end=" ")
		# Cuando termina con la fila usa este print para anular el end= e imprimir la siguiente fila debajo
		print("*")
	print(" 		", end="")
	print("* "*(len(tablero[0])+2))



# -------------------------------------------------------------------------------------------COLOCAR MINAS
def colocar_minas(tablero, minas, fil, col):

	"""COLOCAS LAS MINAS ALEATORIAMENTE EN EL TABLERO

		En tablero al ser una matriz se leen sus coordenada como filas, columnas
		las filas se encuentran el en eje Y
		las columnas o elementos en el eje X
		osea que para situar un elemento accedemos a su posicion en la matriz de esta forma
		(y, x) osea (fila, columna) al la matriz ser una lista de listas anidadas que contiene
		tablero[fila][columna]


		En las matrices las filas son representadas por i
		las columnas son represantadas por j
		de esta manera las coordenadas en una matris son (i, j)
		podrimaos sustituir la "y" por la "i" 
		podriamos sustituir la "x" por la "j"

	"""

	# Lista con las coordenadas de las bombas (y, x) osea (fila, columna)
	minas_ocultas = []
	# Contador de minas colocadas
	numero = 0
	while numero < minas:
		# Fila aleatoria
		y = random.randint(0, fil-1)
		# Columna aleatoria
		x = random.randint(0, col-1)
		# Comprobamos que la coordenada aleatoria no contenga ya una bomba
		# Las bombas se representan con el valor 9
		if tablero[y][x] != 9:
			# Si esta libre la coordenada, colocamos la bomba
			tablero[y][x] = 9
			# Aumentamos contador
			numero+=1
			# Añadimos la coordenada dentro de una tupla y la tupla la añadimos a la lista
			minas_ocultas.append((y, x))
	# Devolvemos el tablero con las minas colocadas y la lista con las coordenadas de las minas
	return tablero, minas_ocultas





# -------------------------------------------------------------------------------------------COLOCAR PISTAS
def colocar_pistas(tablero, filas, columnas):

	"""
		COLOCA LOS NUMEROS QUE INDICAN LAS MINAS CERCANAS

		Recorreremos todo el tablero
	"""
	# Recorremos toda la tabla en busca de minas
	for y in range(filas):
		for x in range(columnas):
			# Si encontramos una mina vamos a recorrer su posiciones adyacentes
			if tablero[y][x] == 9:
				# vamos a mirar en la fila de arriba, la misma fila y la de abajo
				for i in [-1, 0, 1]:
				# Vamos a mirar en la columna anterior el mismo elemento y el siguiente
					for j in [-1, 0, 1]:
						# Combinando comprobamos mediante iteraciones los 3 de la fila de arriba luego los de los lados y luego los de abajo
						# Si el elemento adyacente es menor que 0 o mayor que el indice de filas o columnas no haremos nada ya que esta fuera del tablero
						if 0 <= (y+i) <= filas-1 and 0 <= (x+j) <= columnas-1:
							# Si el elemento adyacente NO es otra mina le sumamos 1 a su valor q incialmente es 0
							if tablero[y+i][x+j] != 9:
								tablero[y+i][x+j] += 1
	"""
		Esto recorrera todos los elementos añacentes a una mina y le sumara 1 a su valor,
		cuando termine con los elementos adyacentes los ciclos i, j habran terminado y pasara a 
		la siguiente mina de esta manera si hay dos minas juntas si un valor que era 0 y una mina 
		se lo ha cambiado al 1, la mina de al lado tbm le sumara otro al estar adyacente a ella tbm
		y se convertira en 2

		Por lo que ar final del bucle tendremos un tablero con las minas y con los valores para sus casillas adyacentes

	"""
	return tablero

# -------------------------------------------------------------------------------------------ALGORITMO RELLENADO
def rellenado(oculto, visible, y, x, filas, columnas, val):
	"""
		RELLENADO DE VALORES PARA LAS CASILLAS DE ALRREDEDOR CON VALOR 0

		Utilizamos el algoritmos de rellenado por difusion on (floodfill)

		Esta funcion consiste en una lista de numero al los que comprobar los alrrededores, esta lista recive
		un primer elemento que es el punto de origen, para comprobar las casillas adyacentes, removemos el
		elemento de la lista con el metodo pop() y lo pasa a las variables y, x que almacenan la ubicacion de un cero,
		ese cero comprueba que valores tiene a su alrrededor y los valores que sean 0 los muestra y los añade a 
		la lista de ceros para que a su vez estos comprueben sus alrrededores en busca de mas ceros, 
		si en lugar de un 0 nos encontramos con otra cosa, (solo puede encontrarse con pistas que vale 1,2,3,4...
		no pued encontrarse con minas pq estes estan rodeadas de pistas) si se encuentran con una pista la muestran
		pero esta al no ser añadida a la lista de ceros no seran comprobados sus alrrededores y esto hara como una barrera
		por donde no se expandira mas el las lista de ceros a comprobar

	"""

	# Esta lista guarda las coordenadas de todos los ceros que vamos a mostrar, ira añadiendo coordenada en cada iteracion
	# Las primeras coordenadas que recive esta lista son los parametros y, x de nuestra posicione actual en el tablero
	# De forma que las primeras coordenadas de esta lista de ceros son las del numero que hemos levantado en el tablero
	ceros = [(y, x)]
	# Mientras que quede algun elemento en la lista de elementos a comprobar
	while len(ceros) > 0:
		# Eliminamos de la lista de elementos a comprobar y pasamos a comprobarlos
		y, x = ceros.pop()
		# Recorremos sus alrrededores como con lo de las pistas, iterando segun su posicion expandiendonos en 1 casilla en todas direcciones
		for i in [-1,0,1]:
			for j in [-1,0,1]:
				# Comprobamos que la casilla a comprobar esta dentro del tablero
				if 0 <= (y+i) <= filas-1 and 0 <= (x+j) <= columnas-1:
					# Si la casilla a comprobar esta sin descubrir y su valor es un 0
					if visible[y+i][x+j] == "-" and oculto[y+i][x+j] == 0:
						# Mostramos un 0 en esa casilla
						visible[y+i][x+j] = 0
						# Comprobamos que la casilla no haya si añadida ya a la lista para no comprobarla dos veces ( Esto provocaria un bucle infinito pq las de los lados se comprobarian unas a otras infinitamente)
						if (y+i, x+j) not in ceros:
							# Añadimos a la lista de casillas a comprobar alrrededores
							ceros.append( (y+i, x+j) )
					# Si la casilla que queremos comprbar no es un 0 osea no esta vacia sino que contiene una pista
					# Mostramos la pista que se encuentra en el tablero oculto
					else:
						visible[y+i][x+j] = oculto[y+i][x+j]

	# Retorna un tablero con las casillas descubiertas por el algoritmo de rellenado
	return visible


# -------------------------------------------------------------------------------------------COMPROBAR COMPLETO

def tablero_completo(tablero, filas, columnas):
	for y in range(filas):
		for x in range(columnas):
			if tablero[y][x] == "-":
				return False

	return True



# -------------------------------------------------------------------------------------------REEMPLAZA LOS CEROS

def reemplazar_ceros(tablero,filas,columnas):
	for i in range(filas):
		for j in range(columnas):
			if tablero[i][j] == 0:
				tablero[i][j] = " "
	return tablero


#############################################FLUJO DEL PROGRAMA####################################################

# Elegimos el tamaño de nuestra matriz
filas = 12
columnas = 16


"""
	Creamos dos tableros, el visible sera el que vea el usuario con el icono y los indicadores de bombas
	el oculto contendra la informacion de donde hay casillas vacias y casillas con bombas
"""

# Creamos un tablero que se mostrara al principio y en las zonas donde no se tenga informacion
visible = crear_tablero(filas, columnas, "-")
# Creamos un tablero que contendra la informacion de las minas y las casillas libres
oculto = crear_tablero(filas, columnas, 0)

# El tablero oculto recive una matriz con las minas colocadas
# Se recive una lista con las ubicaciones de las minas
						# Se pasa el tablero donde se guardaran los datos y el resto de casillas se mantendran intactas
						# Se pasa el numero de minas
						# Se pasa el numero de filas de la matriz
						# Se pasa el munero de columnas de la matriz
oculto, minas_ocultas = colocar_minas(oculto, 15, filas, columnas)

oculto = colocar_pistas(oculto, filas, columnas)


# Mostramos la pantalla de inicio de nuestro juego
presentacion()


# Colocamos la ficha inicial
# Estas variables almacenaran la posicion de la ficha en el tablero
y = random.randint(2, filas-3)
x = random.randint(2, columnas-3)


# Guardamos el valor que tiene la casilla donde se situa nuestra ficha inicial para que cuando nos movamos recupere su valor
real = visible[y][x]
# Sustituimos el valor de la casilla donde hemos aparecido por nuestra x que simula el jugador
visible[y][x] = "x"


# Se borra toda la pantalla de inicio para dar paso al tablero
os.system('cls')


# Mostramos el tablero que donde aparece la ficha y todas las casillas sin descubrir
muestra_tablero(visible)


# BUCLE PRINCIPAL

# Almacena las minas marcadas por el usuario para compararlas con la lista de las ubicaciones de las minas
minas_marcadas = []

# Bandera del bucle principal
jugando = True

while jugando:

	# Preguntamos y almacenamos el movimiento elegida por el jugador el este ciclo
	movimiento = menu()


# ----------------------------------------------------------------------------------------------EJECUTAR CONTROLES

	# Si decide subir
	if movimiento == "w":
		# Si ya estamos arriba del todo
		if y == 0:
			# No hacemos nada
			pass
		# Subir
		else:
			# La casilla de donde venimos recupera su valor
			visible[y][x] = real
			# Cambiamos las posicion del puntero y lo situmaos una fila arriba
			y-=1
			# Guardamos el valor de la casilla donde nos hemos movido
			real = visible[y][x]
			# Mostramos en la casilla nuestra x para indicar que estamos ahi, su valor volvera al movernos
			visible[y][x] = "x"


	# Si decide bajar
	elif movimiento == "s":
		# Si ya esta abajo del todo
		if y == filas-1:
			# Hacemos que su posicion sea la misma con (x = filas-1) o simplemente pass para que no haga nada y no ejecute el else
			pass
		else:
			# Devovelmos su valor a la anterior casilla
			visible[y][x] = real
			# Nos movemos abajo
			y +=1
			# Almacenamos el valor de la casilla de abajo
			real = visible[y][x]
			# Cambiamos el valor por la x
			visible[y][x] = "x"


	# Si quiere ir a la izquierda
	elif movimiento == "a":
		if x == 0:
			pass
		else:
			visible[y][x] = real
			x -= 1
			real = visible[y][x]
			visible[y][x] = "x"



	# Si quiere ir a la derecha
	elif movimiento == "d":
		if  x == columnas-1:
			pass
		else:
			visible[y][x] = real
			x += 1 
			real = visible[y][x]
			visible[y][x] = "x"


	# Si decide marcar una mina
	elif movimiento == "b":
		# Si lo que marca es una casilla oculta y no una pista o una casilla ya descuvierta, etc...
		if real == "-":
			# Hacemos que su valor sea "#"
			visible[y][x] = "#"
			# Cambiamos real para que no cambie al movernos y se quede asi si nos vamos
			real = visible[y][x]
			# Si la casilla no esta en la lista de casillas marcadas
			if (y, x) not in minas_marcadas:
				minas_marcadas.append((y, x))

	# Si decide desmarcar una mina
	elif movimiento == "v":
		if real == "#":
			visible[y][x] = "-"
			real = visible[y][x]
			if (y, x) in minas_marcadas:
				minas_marcadas.remove((y, x))

	# Si elige desvelar la casilla actual
	elif movimiento == "m":
		# Si la casilla es una bomba
		if oculto[y][x] == 9:
			# Cambiamos el valor de la casilla 
			visible[y][x] = "@"
			# Cerramos el bucle pq ha perdido
			jugando = False

		# Si es una pista
		elif oculto[y][x] != 0:
			# Mostramos en el tablero visible, el valor de la casilla en el tablero de pistas
			visible[y][x] = oculto[y][x]
			# Marcamos como real el valor que a aparecido para que no cambie al movernos
			real = visible[y][x]

		# Si es una casilla vacia
		elif oculto[y][x] == 0:
			# Cambiamos el valor por un 0
			visible[y][x] = 0
			# Obtenemos un nuevo tablero con las casilla de alrrededor que sean tbm 0 y las pistas de alrrededor
								# Pasamos el tablero con los datos
								# Pasamos es tablero donde esta nuestro progreso
								# Pasamos nuestra ubicacion y, x
								# Pasamos el tamaños de la matriz filas, columnas
			visible = rellenado(oculto, visible, y, x, filas, columnas, "-")
			visible = reemplazar_ceros(visible, filas, columnas)
			real = visible[y][x]

# --------------------------------------------------------------------------------------------FIN CONTROLES

	# Se limpia la disposicion del tablero anterior y se muestra el tablero con el movimiento realizado
	os.system('cls')
	muestra_tablero(visible)

	ganas = False

	if tablero_completo(visible, filas, columnas) and sorted(minas_ocultas) == sorted(minas_marcadas) and real != "-":
		ganas = True
		jugando = False

if not ganas: 
	print(" 		------------------------")
	print(" 		-------HAS PERDIDO------")
	print(" 		------------------------")

else:
	print(" 		------------------------")
	print(" 		-------HAS GANADO-------")
	print(" 		------------------------")

