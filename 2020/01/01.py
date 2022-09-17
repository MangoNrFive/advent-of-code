import numpy as np
import math


with open('input.txt') as f:
	lines = f.readlines()

arr = []
for line in lines:
	arr.append(line)

arr = [int(arr_element) for arr_element in arr]

count = 0
for idx_1, element_1 in enumerate(arr):
	for element_2 in arr[idx_1:]:
		if element_1 + element_2 == 2020:
			print(element_1 * element_2)
