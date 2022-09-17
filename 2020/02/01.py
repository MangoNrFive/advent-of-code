import numpy as np
import math


with open('input.txt') as f:
	lines = f.readlines()

arr = []
for line in lines:
	arr.append(line)

count = 0
for element in arr:
	rng, char, pw = element.replace(":", "").split()
	rng_split = rng.split("-")
	rng_min = int(rng_split[0])
	rng_max = int(rng_split[1])
	if rng_min <= pw.count(char) <= rng_max:
		count += 1
print(count)
