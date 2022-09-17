import numpy as np
import math
from statistics import median


def main(file):
	with open(file) as f:
		array2d = np.array([[float(digit) for digit in line.replace("\n", "")] for line in f.readlines()])
	
	flash_count = 0
	for step in range(1000):
		array2d += 1

		while True:
			new_flashes = np.argwhere(array2d > 9)
			if not len(new_flashes):
				break
			for new_flash in new_flashes:
				array2d[max(new_flash[0]-1, 0):min(new_flash[0]+2, 10), max(new_flash[1]-1, 0):min(new_flash[1]+2, 10)] += 1
				array2d[new_flash[0]][new_flash[1]] = np.NaN
				flash_count += 1

		if np.isnan(array2d).all():
			print(step+1)
		array2d[np.isnan(array2d)] = 0.0

	print(flash_count)


#main("small_example.txt")
#main("example.txt")
main("input.txt")
