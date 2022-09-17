import numpy as np
import math
from statistics import median
from collections import defaultdict


arr = []
def main(file):
	with open(file) as f:
		lines = f.readlines()
		joind_lines = "".join(lines)
	raw_dots = joind_lines.split("\n\n")[0]
	raw_folds = joind_lines.split("\n\n")[1]

	dots = [(int(element.split(",")[0]), int(element.split(",")[1])) for element in raw_dots.split("\n")]
	folds = [(element.split("=")[0], int(element.split("=")[1])) for element in raw_folds.replace("fold along ", "").split("\n")]

	maxx = max([dot[0] for dot in dots])
	maxy = max([dot[1] for dot in dots])

	maxx = maxx + 1 if maxx % 2 != 0 else maxx
	maxy = maxy + 1 if maxy % 2 != 0 else maxy


	paper = np.full((maxy+1, maxx+1), False)
	for dot in dots:
		paper[dot[1]][dot[0]] = True
	
	for fold in folds:
		if fold[0] == "x":
			left = paper[:,:fold[1]]
			right = paper[:,fold[1]+1:]
			right_flipped = np.flip(right, 1)
			paper = np.logical_or(left, right_flipped)
		elif fold[0] == "y":
			upper = paper[:fold[1],:]
			lower = paper[fold[1]+1:,:]
			lower_flipped = np.flip(lower, 0)
			paper = np.logical_or(upper, lower_flipped)
		else:
			raise Exception
	display = np.full_like(paper, ".", dtype=str)
	display[paper] = "#"
	np.set_printoptions(linewidth=1000)
	print(display)

#main("example.txt")
main("input.txt")
