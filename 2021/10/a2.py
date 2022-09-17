import numpy as np
import math
from statistics import median


def main(file):
	with open(file) as f:
		lines = f.readlines()

	arr = []
	for line in lines:
		arr.append(line.replace("\n",""))

	scores = []
	for row in arr:
		stack = []
		for char in row:
			if char in "}])>":
				opened = stack.pop()
				if char == "}":
					if opened == "{":
						continue
					else:
						points += 1197
						break
				if char == "]":
					if opened == "[":
						continue
					else:
						points += 57
						break
				if char == ")":
					if opened == "(":
						continue
					else:
						points += 3
						break
				if char == ">":
					if opened == "<":
						continue
					else:
						break
				else:
					raise Exception

			elif char in "<([{":
				stack.append(char)
			else:
				raise Exception
		else:
			if stack: # -> incomplete
				points = 0
				for char in reversed(stack):
					points *= 5
					if char == "(":
						points += 1
					elif char == "[":
						points += 2
					elif char == "{":
						points += 3
					elif char == "<":
						points += 4
					else:
						raise Exception
				scores.append(points)
	print(median(scores))
main("example.txt")
main("input.txt")
