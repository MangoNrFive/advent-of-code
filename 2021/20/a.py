import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import ast
from copy import deepcopy


def main(file):
	with open(file) as f:
		lines = f.readlines()
	joined_lines = "".join(lines)
	inputs = joined_lines.split("\n\n")
	IEA = inputs[0]
	image = np.array([[1 if e=="#" else 0 for e in element] for element in inputs[1].split("\n")])

	border = 0
	for i in range(50):
		print(i)
		image = enhance(image, IEA, border)
		border = 0 if border else 1
	print(np.sum(image))


def enhance(image, IEA, border):
	image = np.pad(image, 2, constant_values=border)
	new_image = np.zeros_like(image)
	rows, cols = new_image.shape
	for row in range(1, rows-1):
		for col in range(1, cols-1):
			iea_idx = int("".join(map(str, image[row-1:row+2, col-1:col+2].flatten())), 2)
			new_image[row][col] = 1 if IEA[iea_idx] == "#" else 0
	return new_image[1:-1,1:-1]



#main("example.txt")
main("input.txt")
