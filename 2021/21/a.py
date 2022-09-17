import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import ast
from copy import deepcopy


def main(pos_player_0, pos_player_1):
	score = [0,0]
	position = [pos_player_0, pos_player_1]
	die = roll()

	player = 0
	rolled = 0
	while True:
		dice = next(die) + next(die) + next(die)
		rolled += 3
		position[player] = (position[player] + dice - 1)%10 + 1
		score[player] += position[player]
		if score[player] >= 1000:
			player = 0 if player else 1
			print(score[player] * rolled)
			return
		player = 0 if player else 1



def roll():
	die = 0
	while True:
		die += 1
		yield die
		if die == 100:
			die = 0






#main(4, 8)
main(8, 9)
