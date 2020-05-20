import Santorini_2, time, random2
import concurrent.futures as cf, multiprocessing as mp



game = Santorini_2
start_time = time.time()
all_games = {}



####It inputs into the global dictionary of symmetrical board states
def sym_equivalence(game_state):
    pieceOnTuple = (game_state[1]['a'], game_state[1]['b'], game_state[1]['c'], game_state[1]['d'])
    #print(pieceOnTuple)
    m = [[0,1,2,3,4,5,6,7,8], [2,5,8,1,4,7,0,3,6], [8,7,6,5,4,3,2,1,0], [6,3,0,7,4,1,8,5,2], [2,1,0,5,4,3,8,7,6], [8,5,2,7,4,1,6,3,0], [6,7,8,3,4,5,0,1,2], [0,3,6,1,4,7,2,5,8]]
    #print(''.join([game_state[0][i] for i in m[1]]) + game_state[0][9])
    configs = [''.join([game_state[0][i] for i in j]) + game_state[0][9] for j in m]
    # print(configs)
    all_syms = []
    for config in configs:
    	if str(config) in all_games:
    		continue
    	else:
    		all_games[str([config, game_state[1].copy()])] = all_games[str(game_state)]
    return all_games


###Solver for the game
def Solve(position):
	def game_searcher(game_state, game, depth):
		global all_games
		existsTie = False
		existsWin = False
		print(game_state, depth, game.PrimitiveValue(game_state))
		if game.PrimitiveValue(game_state) == 'lose':
			return 'lose'
		if game.PrimitiveValue(game_state) == 'tie':
			return 'tie'
		if game.PrimitiveValue(game_state) == 'win':
			return 'win'
		for i in game.GenerateMoves(game_state):
			if str(game_state) in all_games:
				return all_games[str(game_state)]
			else:
				copy_game_state = [game_state[0][:], game_state[1].copy()]
				result = game_searcher(game.DoMove(copy_game_state, i), game, depth + 1)
			if result == 'lose': # Other player loses if you make this move, aka you win
				all_games[str(copy_game_state)] = 'win'
				all_games = sym_equivalence(copy_game_state)
				return 'win'
				# existsWin = True
			elif result == 'tie': # Other player ties if you make this move
				existsTie = True
		# if existsWin:
		# 	return 'win'
		if existsTie:
			all_games[str(copy_game_state)] = 'tie'
			# q.put('tie')
			all_games = sym_equivalence(copy_game_state)
			return 'tie'
		else:
			all_games[str(copy_game_state)] = 'lose'
			all_games = sym_equivalence(copy_game_state)
			# q.put('lose')
			return 'lose'
		# return 'tie' if existsTie else 'lose'
	return game_searcher(position, Santorini_2, 0)




### Tells the tier of the board
def tier(game_state):
	tier = 0
	tier +=	 game_state[0].count('1') + 2*game_state[0].count('2') + 3*game_state[0].count('3') + 4*game_state[0].count('4')
	tier += sum([game_state[1][i] for i in game_state[1]])
	return tier


board = ['acbd00000m', {'a': 0, 'b': 0, 'c':2, 'd':0}]
print(Solve(board))



# def multi(game_state):
# 	if __name__ == '__main__':
# 		# q = mp.Queue()
# 		# manager = mp.Manager()
# 		# all_games = manager.dict()
# 		target = 'lose'
# 		found_event = mp.Event()

# 		pool = [mp.Process(target = finder, args = ([game.DoMove([game_state[0][:], game_state[1].copy()], i) for i in game.GenerateMoves(game_state)], target, found_event))]

# 		for p in pool:
# 			p.start()

# 		found_event.wait()
# 		print(pool)
# 		print('{} | terminating processes')
# 		for p in pool:
# 			p.terminate()
# 		for p in pool:
# 			p.join()	



# def multi(game_state):
# 	al = []
# 	if __name__ == '__main__':
# 		with cf.ProcessPoolExecutor() as executor:
# 			subgames = [game.DoMove([game_state[0][:], game_state[1].copy()], i) for i in game.GenerateMoves(game_state)]
# 			results = [executor.submit(Solve, subgames)]
# 			for i in cf.as_completed(results):
# 				al.append(i.result())
# 	return al



# def method(board):
# 	al = []
# 	if __name__ == '__main__':
# 		with cf.ProcessPoolExecutor() as executor:
# 			subgames = [game.DoMove([board[0][:], board[1].copy()], i) for i in game.GenerateMoves(board)]
# 			results = [executor.submit(Solve, subgame) for subgame in subgames]
# 			# print(results)
# 			for f in cf.as_completed(results):
# 				print(f.result())
# 		print('Finished in ' + str(time.time() - start_time) + 's')

# method(board)






