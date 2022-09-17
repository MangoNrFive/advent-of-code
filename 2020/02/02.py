import numpy as np
import math


#file = "input.txt"
file = "example.txt"

with open(file) as f:
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
	if (pw[rng_min-1] == char) != (pw[rng_max-1] == char):
		count += 1
print(count)
