import math, Santorini_2



board = 'abcd10000'
n = int(math.sqrt(len(board)))

vector_direct = {'up': -n, 'upright': -n + 1, 'upleft': -n - 1, 'left': -1, 'downleft': n - 1, 'down': n, 'downright': n + 1, 'right': 1}

all_possible = []


######Finds all permutations of a string
def permutes(board, step = 0):
    if step == len(board):
        # we've gotten to the end, print the permutation
        board = "".join(board)
        if board not in all_possible:
        	if next(board, board.index('a'), '1'):
	        	all_possible.append(board)
        		# print("".join(board))
    for i in range(step, len(board)):
        # copy the string (store as array)
        board_copy = [c for c in board]
         # swap the current index with the step
        board_copy[step], board_copy[i] = board_copy[i], board_copy[step]
         # recurse on the portion of the stringthat has not been swapped yet
        permutes(board_copy, step + 1)




#####Checks within the board if the piece_index is next to a block
def next(string, piece_index, block):
	vectors = vector_direct.copy()
	if piece_index % 3 == 0 and piece_index in [0, 1, 2]:
		del vectors['left']
		del vectors['upleft']
		del vectors['downleft']
		del vectors['up']
		del vectors['upright']
	if piece_index % 3 == 0 and piece_index in [6,7,8]:
		del vectors['left']
		del vectors['upleft']
		del vectors['downleft']
		del vectors['down']
		del vectors['downright']
	if piece_index % 3 == 2 and piece_index in [0,1,2]:
		del vectors['upright']
		del vectors['right']
		del vectors['downright']
		del vectors['up']
		del vectors['upleft']
	if piece_index % 3 == 2 and piece_index in [6,7,8]:
		del vectors['upright']
		del vectors['right']
		del vectors['downright']
		del vectors['down']
		del vectors['downleft']
	if piece_index % 3 == 0 and 'left' in vectors:
		del vectors['left']
		del vectors['upleft']
		del vectors['downleft']
	if piece_index % 3 == 2 and 'right' in vectors:
		del vectors['upright']
		del vectors['right']
		del vectors['downright']
	if piece_index in [0,1,2] and 'up' in vectors:
		del vectors['up']
		del vectors['upright']
		del vectors['upleft']
	if piece_index in [6,7,8] and 'down' in vectors:
		del vectors['down']
		del vectors['downright']
		del vectors['downleft']
	indices = [piece_index + vectors[i] for i in vectors if piece_index + vectors[i] >= 0 and piece_index + vectors[i] < len(board)]
	return any([string[i] == block for i in indices])



def tier_cardinality(board):
	permutes(board)
	return len(all_possible)/4







########Finds all partitions of a number O(n^2)
# def all_partitions(number):
#     answer = []
#     answer.append([number, ])
#     for x in range(1, number):
#         for y in all_partitions(number - x):
#             answer.append(list(sorted([x, ] + y)))
#     return answer


#########Much faster runtime O(n)
def all_partitions(n, I=1):
    yield [n,]
    for i in range(I, n//2 + 1):
        for p in all_partitions(n-i, i):
            yield [i,] + p


#######Gets rid of repeats within all_partitions
def filter_repeats(partitions):
	partitions = [str(i) for i in partitions]
	partitions = list(dict.fromkeys(partitions))
	partitions = [eval(i) for i in partitions]
	return partitions


#######Finds all partitions given the constraints of the game
def size_partitions(partitions, number, size):
	rid1 = [i for i in partitions if not (i.count(1) <= 9 and i.count(2) <= 9 and i.count(3) <= 9 and i.count(4) <= 9)]
	outliers = [i for i in range(size + 1, number + 1)]
	rid2 = [i for i in partitions for j in outliers if i.count(j) > 0]
	rid3 = [i for i in partitions if len(i) > 9]
	return [i for i in partitions if i not in rid1 + rid2 + rid3]



######This counts the number of partitions given the max pieces size
def partitions(num, size):
	if num == 0:
		return 1
	elif num < 0:
		return 0
	if size == 0:
		return 0
	return partitions(num, size - 1) + partitions(num - size, size)






####Terminal
print(tier_cardinality(board))



#### Finding all the partitions. i.e. all possible combinations of putting the n-th piece on the board
#		There are strictions on to which pieces do
# n = 5
# print(filter_repeats(all_partitions(n)))
# print()
# print(size_partitions(filter_repeats(all_partitions(n)), n, 4))

# print(partitions(n, n))
# print(len(list(parts(n))))
# print(list(parts(n)))



