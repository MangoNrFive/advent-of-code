import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import pyastar2d


arr = []
def main(file):
	np.set_printoptions(threshold=np.inf)

	with open(file) as f:
		weights = np.array([[int(digit) for digit in line.replace("\n", "")] for line in f.readlines()], dtype=np.float32)

	rows_o, cols_o = weights.shape

	weights_big = np.tile(weights, (5,5))
	for row in range(5):
		for col in range(5):
			weights_big[rows_o*row:rows_o*(row+1), cols_o*col:cols_o*(col+1)] += row + col

	weights_big[weights_big>9] -= 9

	path = pyastar2d.astar_path(weights_big, (0, 0), (weights_big.shape[0]-1, weights_big.shape[1]-1), allow_diagonal=False)

	risk = 0
	for pos in path:
		risk += weights_big[pos[0]][pos[1]]
	risk -= weights_big[0][0]

	print(risk)

#main("example.txt")
main("input.txt")
