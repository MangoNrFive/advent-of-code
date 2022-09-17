import numpy as np
import math


with open('input.txt') as f:
	lines = f.readlines()

arr = []
for line in lines:
	arr.append(line)

arr = [int(arr_element) for arr_element in arr]

count = 0
for idx in range(len(arr) - 1):
	if arr[idx+1] > arr[idx]:
		count += 1
print(count)
