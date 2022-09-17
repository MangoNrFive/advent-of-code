import numpy as np
import math


def main(file):
	with open(file) as f:
		lines = f.readlines()

	arr = []
	for line in lines:
		arr.append(line.replace("\n",""))

	points = 0
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
						points += 25137
						break
				else:
					raise Exception

			elif char in "<([{":
				stack.append(char)
			else:
				raise Exception

	print(points)
main("example.txt")
main("input.txt")
