import numpy as np
import math


#file = "input.txt"
file = "example.txt"

with open(file) as f:
	lines = f.readlines()

arr = []
for line in lines:
	arr.append(line)

depth = 0
horizontal = 0
aim = 0
for element in arr:
	(direction, length) = element.split() 
	if direction == "up":
		aim -= int(length)
	if direction == "down":
		aim += int(length)
	if direction == "forward":
		horizontal += int(length)
		depth += int(length)*aim
print(horizontal * depth)
