import random

boardSize = (10,10)

orientation = 0

shipSizes = {
	"Carrier":    5,
	"battleShip": 4,
	"cruiser":    3,
	"submarine":  3,
	"destroyer":  2
}

def checkLose(board,ships):
	lost = True
	for ship in ships:
		for line in board:
			if ship[0] in line:
				lost = False
	return lost

def draw():
	print("\nAI:")
	dispBoard(aiBoard,False)
	print("Player:")
	dispBoard(playerBoard,True)

def dispBoard(board,showShips):
	print("\n    0 1 2 3 4 5 6 7 8 9\n")
	l = 0
	if showShips:
		for line in board:
			print(l,end="   ")
			for place in line:
				print(place,end=" ")
			l = l + 1
			print("")
	else:
		for line in board:
			print(l,end="   ")
			for place in line:
				if place == "." or place == "/" or place == "X":
					print(place,end=" ")
				else:
					print(".",end=" ")
			l = l + 1
			print("")
	print("\n\n")

def generateBoard(size):
	board = []
	for x in range(size[0]):
		line = []
		for y in range(size[1]):
			line.append(".")
		board.append(line)
	return board

def placeShips(ships,board):
	for ship in ships:
		success = False
		while not success:
			#print("placing "+ship)
			orientation = random.randint(0,1)
			colision = False
			if orientation == 0:
				coords = [random.randint(0,boardSize[0]),random.randint(0,boardSize[1]-ships[ship])]
				for pos in range(0,ships[ship]):
					if board[coords[0]-1][coords[1]+pos] != ".":
						colision = True
				if not colision:
					for pos in range(0,ships[ship]):
						board[coords[0]-1][coords[1]+pos]=ship[0]
					success = True
			else:
				coords = [random.randint(0,boardSize[0]-ships[ship]),random.randint(0,boardSize[1])]
				for pos in range(0,ships[ship]):
					if board[coords[0]+pos][coords[1]-1] != ".":
						colision = True
				if not colision:
					for pos in range(0,ships[ship]):
						board[coords[0]+pos][coords[1]-1]=ship[0]
					success = True
	return board

try:
	auto = input("Would you like your board to be generated automatically? (Y/n) ").lower()[0]
except:
	auto = "y"

aiBoard = placeShips(shipSizes,generateBoard(boardSize))

if auto != "n":
	playerBoard = placeShips(shipSizes,generateBoard(boardSize))
else:
	print("Too bad because self generated boards are not supported yet...")
	playerBoard = placeShips(shipSizes,generateBoard(boardSize))

winner = False

while not winner:
	while True:
		draw()
		try:
			x,y = input("Please input your move in the format \"x,y\" (exclude the quotation marks): ").replace(" ","").split(",")
			y,x = int(x),int(y)
			if x < boardSize[0] and x > -1 and y < boardSize[1] and y > -1:
				break
			else:
				print("Out of bounds...")
		except KeyboardInterrupt:
			print("\nClosing...")
			quit()
		except:
			print("Invalid format...")
	if aiBoard[x][y] != "." and aiBoard[x][y] != "/":
		if aiBoard[x][y] != "X":
			aiBoard[x][y] = "X"
			print("Hit!")
		else:
			print("Already Hit...")
	else:
		aiBoard[x][y] = "/"
		print("Miss...")
	x,y = random.randint(0,9),random.randint(0,9)
	if playerBoard[x][y] != "." and playerBoard[x][y] != "/":
		if playerBoard[x][y] != "X":
			playerBoard[x][y] = "X"
	else:
		playerBoard[x][y] = "/"
	if checkLose(playerBoard,shipSizes):
		winner = "The AI"
	elif checkLose(aiBoard,shipSizes):
		winner = "Player"

print(winner+" won!!!")