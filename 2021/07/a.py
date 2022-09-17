import numpy as np
from numpy import mean, absolute
import math


def mad(data, axis=None):
    return mean(absolute(data), axis)


def main(file):
	with open(file) as f:
		lines = f.readlines()

	input_str = "".join(lines)
	arr = np.array([int(element) for element in input_str.split(",")])

	fuels = [] 
	for position in range(max(arr)):
		diffs = [n**2/2 + absolute(n)/2 for n in arr-position]
		fuels.append(sum(absolute(diffs)))

	print(min(fuels))

main("example.txt")
main("input.txt")
