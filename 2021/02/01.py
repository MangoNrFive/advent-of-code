import numpy as np
import math


with open('input.txt') as f:
	lines = f.readlines()

arr = []
for line in lines:
	arr.append(line)

depth = 0
horizontal = 0
for element in arr:
	(direction, length) = element.split() 
	if direction == "up":
		depth += int(length)
	if direction == "down":
		depth -= int(length)
	if direction == "forward":
		horizontal += int(length)
print(horizontal * depth)
