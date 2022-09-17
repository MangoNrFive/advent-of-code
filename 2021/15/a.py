import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import pyastar2d


arr = []
def main(file):
	with open(file) as f:
		weights = np.array([[int(digit) for digit in line.replace("\n", "")] for line in f.readlines()], dtype=np.float32)
	
	path = pyastar2d.astar_path(weights, (0, 0), (weights.shape[0]-1, weights.shape[1]-1), allow_diagonal=False)

	risk = 0
	for pos in path:
		risk += weights[pos[0]][pos[1]]
	risk -= weights[0][0]

	print(risk)

#main("example.txt")
main("input.txt")
