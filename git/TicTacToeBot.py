import TicTacToe, Santorini_Solver, Santorini_2, random2, time

game = Santorini_2
first = True


#####Generates all the best possible moves
# def GenMoves(position):
# 	possibles = []
# 	if Santorini_Solver.Solve(position) == 'win':
# 		possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose']
# 	elif Santorini_Solver.Solve(position) == 'tie':
# 		possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose' or Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'tie']
# 	elif Santorini_Solver.Solve(position) == 'lose':
# 		possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose' or Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'tie' or Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'win']
# 	return possibles


#####Tells the tier of the game
def tier(game_state):
	tier = 0
	tier = tier + game_state[0].count('1') + 2*game_state[0].count('2') + 3*game_state[0].count('3') + 4*game_state[0].count('4')
	tier += sum([game_state[1][i] for i in game_state[1]])
	return tier




#####Automatically generates possible moves and chooses one at random to move
def auto_move(position):
	possibles = []
	startTime = 
	if tier(position) < 11:
		copy_position = []
		if position[0][len(position[0])-1] == 'm':
			copy_position = [position[0][:len(position[0]) - 1] + 'n', position[1].copy()]
		elif position[0][len(position[0])-1] == 'n':
			copy_position = [position[0][:len(position[0]) - 1] + 'm', position[1].copy()]
		losing = []
		for i in game.GenerateMoves(copy_position):
			if game.PrimitiveValue(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose':
				losing.append(i)
		getTo = [i[0] + game.directions[i[1][0]] for i in losing] 
		possibles = [i for i in game.GenerateMoves(position) for j in getTo if i[0] + game.directions[i[1][0]] + game.directions[i[1][1]] == j]
		if not possibles:
			possibles = game.GenerateMoves(position)
	else:		
		result = Santorini_Solver.Solve(position)
		if result == 'lose':
			possibles = game.GenerateMoves(position)
		elif result == 'win':
			possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose']
		elif result == 'tie':
			possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose' or Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'tie']
	random_best = random2.randint(0, len(possibles) - 1)
	position = game.DoMove([position[0][:], position[1].copy()], possibles[random_best])
	# print(possibles, random_best)
	return position




def move(position, move = None):
	possibles = []
	position = game.DoMove([position[0][:], position[1].copy()], move)
	# elif position[0][9] == 'n':
	# 	# print(Santorini_Solver.Solve(position))
	# 	if Santorini_Solver.Solve(position) == 'win':
	# 		possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose']
	# 	elif Santorini_Solver.Solve(position) == 'tie':
	# 		possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose' or Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'tie']
	# 	elif Santorini_Solver.Solve(position) == 'lose':
	# 		possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'lose' or Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'tie' or Santorini_Solver.Solve(game.DoMove([position[0][:], position[1].copy()], i)) == 'win']
	# 	position = game.DoMove([position[0][:], position[1].copy()], possibles[0])
		# print(possibles[0])
	return position

# def move(position, move = None):
# 	possibles = []
# 	if position[9] == 'a':
# 		position = game.DoMove(position, move)
# 	elif position[9] == 'b':
# 		# print(Santorini_Solver.Solve(position))
# 		if Santorini_Solver.Solve(position) == 'win':
# 			possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove(position, i)) == 'lose']
# 		if Santorini_Solver.Solve(position) == 'tie':
# 			possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove(position, i)) == 'lose' or Santorini_Solver.Solve(game.DoMove(position, i)) == 'tie']
# 		if Santorini_Solver.Solve(position) == 'lose':
# 			possibles = [i for i in game.GenerateMoves(position) if Santorini_Solver.Solve(game.DoMove(position, i)) == 'lose' or Santorini_Solver.Solve(game.DoMove(position, i)) == 'tie' or Santorini_Solver.Solve(game.DoMove(position, i)) == 'win']
# 		# print(possibles)
# 		position = game.DoMove(position, possibles[0])
# 	return position








def prnt_board(board):
	counter = 0
	for _ in range(3):
		print(board[counter] + ' | ' + board[counter + 1] + ' | ' + board[counter + 2])
		counter += 3


#Terminal


############Just give out the good moves for a board state



on = False
print('Lets play this game! ')
start = input('ready? ')



# #########Auto Play
# if start == 'yes':
# 	choice = input('First or second? ')
# 	on = not on
# 	# board = ['a4c1023dbn', {'a': 0, 'b': 2, 'c': 0, 'd': 1}]
# 	board = ['a0b000d0cm', {'a': 0, 'b': 0, 'c': 0, 'd': 0}]
# 	prnt_board(board[0])
# 	print(board[1])
# 	while on:
# 		print()
# 		board = auto_move(board)
# 		prnt_board(board[0])
# 		print(board[1])
# 		print()
# 		if game.PrimitiveValue(board) != 'undecided':
# 			if choice == 'first':
# 				print('You win!')
# 			if choice == 'second':
# 				print('You lose!')
# 			break
# 		board = auto_move(board)
# 		prnt_board(board[0])
# 		print(board[1])
# 		print()
# 		if game.PrimitiveValue(board) != 'undecided':
# 			if choice == 'first':
# 				print('You lose!')
# 			if choice == 'second':
# 				print('You win!')
# 			break


def display_moves_and_execute(game_state):
	lst = []
	for i in range(len(game.GenerateMoves(game_state))):
		lst.append(str(i) + ' ' + str(game.GenerateMoves(game_state)[i]))
	print(lst)
	index = input('choose based on index of list: ')
	print()
	return game.GenerateMoves(game_state)[eval(index)]






#####Santorini
if start == 'yes':
	on = not on
	board = ['a0b000d0cm', {'a': 0, 'b': 0, 'c': 0, 'd': 0}]
	print()
	prnt_board(board[0])
	print(board[1])
	print()
	choice = input('First or second? ')
	while on:
		if choice == 'first':
			print()
			movement = display_moves_and_execute(board)
			board = move(board, movement)
			prnt_board(board[0])
			print(board[1])
			print()
			if game.PrimitiveValue(board) != 'undecided':
				if game.PrimitiveValue(board) == 'tie':
					print('You tied!')
					break
				print('You win!')
				break
			board = auto_move(board)
			prnt_board(board[0])
			print(board[1])
			print()
			if game.PrimitiveValue(board) != 'undecided':
				if game.PrimitiveValue(board) == 'tie':
					print('You tied!')
					break
				print('You lose!')
				break
		elif choice == 'second':
			board = auto_move(board)
			print()
			prnt_board(board[0])
			print(board[1])
			print()
			if game.PrimitiveValue(board) != 'undecided':
				if game.PrimitiveValue(board) == 'tie':
					print('You tied!')
					break
				print('You lose!')
				break
			movement = display_moves_and_execute(board)
			board = move(board,movement)
			prnt_board(board[0])
			print(board[1])
			print()
			if game.PrimitiveValue(board) != 'undecided':
				if game.PrimitiveValue(board) == 'tie':
					print('You tied!')
					break
				print('You win!')
				break




# if start == 'yes':
# 	on = not on
# 	board = '123456789a'
# 	prnt_board(board)
# 	choice = input('First or second? ')
# 	while on:
# 		if choice == 'first':
# 			print()
# 			movement = input('Choose a space: ')
# 			board = move(board, eval(movement))
# 			if game.PrimitiveValue(board) != 'undecided':
# 				if game.PrimitiveValue(board) == 'tie':
# 					print('You tied!')
# 					break
# 				print('You ' + str(game.PrimitiveValue(board)) + '!')
# 				break
# 			prnt_board(board)
# 			print()
# 			board = move(board)
# 			prnt_board(board)
# 			print()
# 			if game.PrimitiveValue(board) != 'undecided':
# 				if game.PrimitiveValue(board) == 'tie':
# 					print('You tied!')
# 					break
# 				print('You ' + str(game.PrimitiveValue(board)) + '!')
# 				break
# 		elif choice == 'second':
# 			board = board[:len(board) - 1] + 'b'
# 			board = move(board)
# 			print()
# 			prnt_board(board)
# 			print()
# 			if game.PrimitiveValue(board) != 'undecided':
# 				if game.PrimitiveValue(board) == 'tie':
# 					print('You tied!')
# 					break
# 				print('You ' + str(game.PrimitiveValue(board)) + '!')
# 				break
# 			movement = input('Choose a space: ')
# 			board = move(board, eval(movement))
# 			prnt_board(board)
# 			print()
# 			if game.PrimitiveValue(board) != 'undecided':
# 				if game.PrimitiveValue(board) == 'tie':
# 					print('You tied!')
# 					break
# 				print('You ' + str(game.PrimitiveValue(board)) + '!')
# 				break
