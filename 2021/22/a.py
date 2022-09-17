import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import ast
from copy import deepcopy


def main(file):
	with open(file) as f:
		lines = f.readlines()
	instructions = []
	for line in lines:
		split_space = line.replace("\n", "").split(" ")
		status = 1 if split_space[0] == "on" else 0
		coordinates = split_space[1].split(",")
		x = [int(e) + 50 for e in coordinates[0].replace("x=", "").split("..")]
		y = [int(e) + 50 for e in coordinates[1].replace("y=", "").split("..")]
		z = [int(e) + 50 for e in coordinates[2].replace("z=", "").split("..")]
		instructions.append([
			status,
			x,
			y,
			z,
			])

	reactor = np.zeros((101,101,101))
	for inst in instructions:
		print(inst)
		reactor[inst[1][0]:inst[1][1]+1, inst[2][0]:inst[2][1]+1, inst[3][0]:inst[3][1]+1] = inst[0]
	print(np.sum(reactor))




#main("example_1.txt")
#main("example_2.txt")
main("input.txt")
