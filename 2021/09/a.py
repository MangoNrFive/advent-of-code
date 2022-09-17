import numpy as np
import math


def main(file):
	with open(file) as f:
		array2d = np.array([[int(digit) for digit in line.replace("\n", "")] for line in f.readlines()])

	p = np.pad(array2d, 1, constant_values=10)
	n = np.roll(p, -1, axis=0)
	e = np.roll(p, 1, axis=1)
	s = np.roll(p, 1, axis=0)
	w = np.roll(p, -1, axis=1)
	low = np.logical_and(np.logical_and(np.logical_and(p < n, p < e), p < s), p < w)
	print(np.sum(p+1, where=low))


main("example.txt")
#main("input.txt")
