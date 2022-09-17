import numpy as np
import math

from scipy import ndimage


def main(file):
	with open(file) as f:
		array2d = np.array([[int(digit) for digit in line.replace("\n", "")] for line in f.readlines()])

	print(array2d < 9)
	labeled, num_objects = ndimage.label(array2d < 9)
	slices = ndimage.find_objects(labeled)

	ones = np.ones_like(labeled)

	sizes = []
	for i in range(1, num_objects+1):
		sizes.append(sum(ones[np.where(labeled == i)]))

	print(sorted(sizes)[-1] * sorted(sizes)[-2] * sorted(sizes)[-3])


main("example.txt")
#main("input.txt")
