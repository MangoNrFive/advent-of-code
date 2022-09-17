import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import ast
from copy import deepcopy
from time import perf_counter


WINS = [0,0]
branches = [
	(3, 1),
	(4, 3),
	(5, 6),
	(6, 7),
	(7, 6),
	(8, 3),
	(9, 1),
]


def main(pos_player_0, pos_player_1):
	score = [0,0]
	position = [pos_player_0, pos_player_1]
	player = 0

	roll(player, score, position, 1)
	print(WINS)


def roll(player, sc, pos, factor):
	global WINS
	
	new_player = 0 if player else 1
	for branch in branches:
		position = pos[:]
		position[player] = (position[player] + branch[0] - 1)%10 + 1
		score = sc[:]
		score[player] += position[player]

		if score[player] >= 21:
			WINS[player] += factor*branch[1]
		else:
			roll(new_player, score, position, factor*branch[1])






#main(4, 8)
main(8, 9)