import math



bD = 'a0b000d0cm'
pO = {'a':0, 'b':0, 'c':0, 'd':0}
board_value = [bD, pO]



n = int(math.sqrt(len(bD) - 1))
directions = {'up': -n, 'upright': -n + 1, 'upleft': -n - 1, 'left': -1, 'downleft': n - 1, 'down': n, 'downright': n + 1, 'right': 1}



def DoMove(board_value, move):
	board = board_value[0]
	pieceOn = board_value[1]
	piece = board[move[0]]
	board = board.replace(piece, str(pieceOn[piece]))
	moveToIndex = move[0] + directions[move[1][0]]
	buildIndex = moveToIndex + directions[move[1][1]]
	pieceOn[piece] = eval(board[moveToIndex])
	board = board[:moveToIndex] + piece + board[moveToIndex + 1:]
	board = board[:buildIndex] + str(eval(board[buildIndex]) + 1) + board[buildIndex + 1:]
	if board[9] == 'm':
		board = board[:len(board) - 1] + 'n'
	elif board[9] == 'n':
		board = board[:len(board) - 1] + 'm'
	return [board[:], pieceOn.copy()]





def GenerateMoves(board_value):
	board = board_value[0]
	pieceOn = board_value[1]
	index_track = []
	if board[9] == 'm':
		for i in board:
			if i == 'a' or i == 'c':
				index_track.append(board.find(i))
	elif board[9] == 'n':
		for i in board:
			if i == 'b' or i == 'd':
				index_track.append(board.find(i))
	list1 = [[index_track[0], i] for i in GenPiece([board, pieceOn], index_track[0])]
	list2 = [[index_track[1], i] for i in GenPiece([board, pieceOn], index_track[1])]
	return list1 + list2



def PrimitiveValue(board_value):
	board = board_value[0]
	pieceOn = board_value[1]
	if any([pieceOn[i] == 3 for i in pieceOn]) or not GenerateMoves(board_value):
		return 'lose'
	return 'undecided'




### Helper Functions


#See if a player can move with either piece
def GenPiece(board_value, piece):
	board = board_value[0][:len(board_value[0]) - 1]
	pieceOn = board_value[1]
	possible_moves = [[i, j] for i in directions for j in directions]
	elimRight = ['right', 'upright', 'downright']
	elimLeft = ['left', 'upleft', 'downleft']
	elimUp = ['up', 'upright', 'upleft']
	elimDown = ['down', 'downright', 'downleft']
	if piece % 3 == 0:
		complement = [i for i in possible_moves if i[0] in elimLeft or ((i[0] == 'up' or i[0] == 'down') and i[1] in elimLeft)]
		possible_moves = [i for i in possible_moves if i not in complement]
	if piece % 3 == 2:
		complement = [i for i in possible_moves if i[0] in elimRight or ((i[0] =='up' or i[0] == 'down' ) and i[1] in elimRight)]
		possible_moves = [i for i in possible_moves if i not in complement]
	if piece in [i for i in range(n)]:
		complement = [i for i in possible_moves if i[0] in elimUp or (i[1] in elimUp and (i[0] == 'right' or i[0] == 'left'))]
		possible_moves = [i for i in possible_moves if i not in complement]
	if piece in [len(board) - (i+1) for i in range(n)]:
		complement = [i for i in possible_moves if i[0] in elimDown or (i[1] in elimDown and (i[0] == 'right' or i[0] == 'left'))]
		possible_moves = [i for i in possible_moves if i not in complement]
	complement = []
	for i in possible_moves:
		if piece + directions[i[0]] + directions[i[1]] < 0 or piece + directions[i[0]] + directions[i[1]] >= len(board):
			complement.append(i)
		elif board[piece + directions[i[0]] + directions[i[1]]] in pieceOn and board[piece] != board[piece + directions[i[0]] + directions[i[1]]]:
			complement.append(i)
		elif board[piece + directions[i[0]] + directions[i[1]]] not in pieceOn and eval(board[piece + directions[i[0]] + directions[i[1]]]) == 4:
			complement.append(i)
	possible_moves = [i for i in possible_moves if i not in complement]
	for i in possible_moves:
		if board[piece + directions[i[0]]] in pieceOn:
			complement.append(i)
	possible_moves = [i for i in possible_moves if i not in complement]
	complement = []
	for i in possible_moves:
		if eval(board[piece + directions[i[0]]]) > 1 + pieceOn[board[piece]]:
			complement.append(i)
	possible_moves = [i for i in possible_moves if i not in complement]


	complement = []
	for i in possible_moves:
		if piece + directions[i[0]] % 3 == 0:
			if i[1] in elimLeft:
				complement.append(i)
		if piece + directions[i[0]] % 3 == 2:
			if i[1] in elimRight:
				complement.append(i)
		if piece + directions[i[0]] in [0,1,2]:
			if i[1] in elimUp:
				complement.append(i)
		if piece + directions[i[0]] in [6,7,8]:
			if i[1] in elimDown:
				complement.append(i)
	possible_moves = [i for i in possible_moves if i not in complement]

	complement = []
	for i in possible_moves:
		if piece in [3,4,5]:
			if i[0] in elimDown and i[1] in elimDown:
				complement.append(i)
			if i[0] in elimUp and i[1] in elimUp:
				complement.append(i)
		if piece % 3 == 1:
			if i[0] in elimRight and i[1] in elimRight:
				complement.append(i)
			if i[0] in elimLeft and i[1] in elimLeft:
				complement.append(i)

	possible_moves = [i for i in possible_moves if i not in complement]

	return possible_moves






#Just to print and see the board state easier
def prnt_board(board):
	counter = 0
	for _ in range(n):
		print(board[counter] + ' | ' + board[counter + 1] + ' | ' + board[counter + 2])
		counter += 3



## Terminal
print(Solve(['a0b000d0cm', {'a':0, 'b':0, 'c':0, 'd':0}]))
