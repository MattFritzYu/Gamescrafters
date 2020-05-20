import Santorini_2, random2, time

start_time = time.time()

game = Santorini_2
single_tier_counter = []




start_state = ['10ba00d0cn', {'a': 0, 'b': 0, 'c': 0, 'd': 0}]


def random_tierN_board_generator(n):
	current_state = start_state
	copyN = n
	while copyN > 0:
		all_moves = game.GenerateMoves(current_state)
		# print(len(all_moves))
		random_index = random2.randint(0, len(all_moves) - 1)
		current_state = Santorini_2.DoMove([current_state[0][:], current_state[1].copy()], all_moves[random_index])
		copyN -= 1
	if game.PrimitiveValue(current_state) != 'undecided' and current_state[0].count('3') > 0 and current_state[0].count('4') > 0:
		return random_tierN_board_generator(n)
	return current_state




print(random_tierN_board_generator(10))

def tier_n(list_game_state):
	l = 0
	all_games = []
	for i in list_game_state:
		for j in game.GenerateMoves(i):
			all_games.append(game.DoMove(i, j))
			# l += 1
			# print(l)
	# print(len(all_games))
	return all_games


def all_tiers(list_game_state, n):
	tier = 1
	tier_value = [start_state]
	while tier <= n:
		print('Tier ' + str(tier) + ': ' + str(len(tier_n(tier_value))))
		tier += 1
		tier_value = tier_n(tier_value)


# all_tiers([start_state], 5)


# print(tier_n(tier_n(tier_n(tier_n([start_state])))))



#  







# Solve(['a0b000d0cm', {'a': 0, 'b': 0, 'c': 0, 'd': 0}])
# print(single_tier_counter)
# print(len(single_tier_counter))



print('Finished in ' + str((time.time() - start_time)) + ' seconds')