import pygame, math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('PathFinder')

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot():
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	# Obtiene la coordenadas del nodo
	def get_pos(self):
		return self.row, self.col

	# Retorna si el nodo ya ha sido calculado como posible ruta
	def is_closed(self):
		# Retorna True or False dependiendo de la condicion
		return self.color == RED

	# Retorna si esta en el set de nodos cercano que todavia no han sido calculados
	def is_open(self):
		return self.color == GREEN


	def is_barrier(self):
		return self.color == BLACK


	def is_start(self):
		return self.color == ORANGE


	def is_end(self):
		return self.color == TURQUOISE


	def reset(self):
		self.color = WHITE


	def make_closed(self):
		self.color = RED


	def make_open(self):
		self.color = GREEN


	def make_barrier(self):
		self.color = BLACK


	def make_closed(self):
		self.color = RED


	def make_start(self):
		self.color = ORANGE


	def make_end(self):
		self.color = TURQUOISE


	def make_path(self):
		self.color = PURPLE


	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	# Comprueba NSEW si son o no barrera y si NO son las añade a la lista de neighbors
	def update_neighbors(self, grid):
		self.neighbors = [] 


		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

	def __lt__(self, other):
		return False


# Calcula la distancia entre dos puntos
# Esta funcion una el metodo de manhattan para calcular distancias
# Lo usaremos para suponer la distancia con el nodo final ya que todavia no conocemos en camino por lo que no podemos saber la distancia exacta
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2

	# Retorna el valor absoluto en pasos en ambos ejes
	return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			start.make_start()
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False

# Crea un DataFrame que es un array bidimensional con los spots
def make_grid(rows, width):
	grid = []
	tamaño_celda = width // rows

	for row in range(rows):
		grid.append([])
		for col in range(rows):
			spot = Spot(row, col, tamaño_celda, rows)
			grid[row].append(spot)


	return grid

# Pinta las lineas grises de la cuadricula en la ventana
def draw_grid(win, rows, width):
	tamaño_celda = width // rows

	for row in range(rows):
		pygame.draw.line(win, GREY, (0, row*tamaño_celda), (width, row*tamaño_celda))
		pygame.draw.line(win, GREY, (row*tamaño_celda, 0), (row*tamaño_celda, width))

# Pinta cada spot con su informacion de color y las lineas de la cuadricula
def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


# Obtiene la posicion del mause, calcula la celda clicado y retorna las coordenadas de la celda
def get_clicked_pos(pos, rows, width):
	tamaño_celda = width // rows
	y, x = pos

	row = y // tamaño_celda
	col = x // tamaño_celda

	return row, col

# MAIN LOOP
def main(win, width):
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None # Nodo inicio
	end = None # Nodo  final

	run = True # Ejecucion del programa

	while run:
		draw(win, grid, ROWS, width)
		# Manejo de eventos en la ventana
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: #LEFT MOUSE
				pos = pygame.mouse.get_pos()
				print('POS: ', pos)
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]

				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				print('POS: ', pos)
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()

				if spot == start:
					start = None
				elif spot == end:
					end = None
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

	pygame.quit()


main(WIN, WIDTH)