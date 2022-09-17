import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import ast
from copy import deepcopy


# [[x, sign_x], [y, sign_y], [z, sign_z]],
# 0 -> x
# 1 -> y
# 2 -> z
MAPPINGS = [
	# X -> X
	[[ 0, 1], [ 1, 1], [ 2, 1]],
	[[ 0, 1], [ 2,-1], [ 1, 1]],
	[[ 0, 1], [ 1,-1], [ 2,-1]],
	[[ 0, 1], [ 2, 1], [ 1,-1]],
	[[ 0,-1], [ 2, 1], [ 1, 1]],
	[[ 0,-1], [ 1, 1], [ 2,-1]],
	[[ 0,-1], [ 2,-1], [ 1,-1]],
	[[ 0,-1], [ 1,-1], [ 2, 1]],

	# Y -> X
	[[ 1, 1], [ 2, 1], [ 0, 1]],
	[[ 1, 1], [ 0,-1], [ 2, 1]],
	[[ 1, 1], [ 2,-1], [ 0,-1]],
	[[ 1, 1], [ 0, 1], [ 2,-1]],
	[[ 1,-1], [ 0, 1], [ 2, 1]],
	[[ 1,-1], [ 2, 1], [ 0,-1]],
	[[ 1,-1], [ 0,-1], [ 2,-1]],
	[[ 1,-1], [ 2,-1], [ 0, 1]],

	# Z -> X
	[[ 2, 1], [ 0, 1], [ 1, 1]],
	[[ 2, 1], [ 1,-1], [ 0, 1]],
	[[ 2, 1], [ 0,-1], [ 1,-1]],
	[[ 2, 1], [ 1, 1], [ 0,-1]],
	[[ 2,-1], [ 1, 1], [ 0, 1]],
	[[ 2,-1], [ 0, 1], [ 1,-1]],
	[[ 2,-1], [ 1,-1], [ 0,-1]],
	[[ 2,-1], [ 0,-1], [ 1, 1]],
]


def main(file):
	with open(file) as f:
		lines = f.readlines()
	joined_lines = "".join(lines)
	scanners = [np.array([(0,0,0) for e in joined_line.split("\n")[1:]]) for joined_line in joined_lines.split("\n\n")]
	scanners = [a[np.lexsort((a[:,2], a[:,1],a[:,0]))][::-1] for idx, a in enumerate(scanners)]


	with open("out.txt") as f:
		lines = f.readlines()
	joined_lines = "".join(lines)
	steps = joined_lines.split("\n\n\n")
	instructions = []
	for step in steps:
		splitted = step.split("\n")
		scanner_from = int(splitted[0].replace("scanner", "").split(" -> ")[0])
		scanner_to = int(splitted[0].replace("scanner", "").split(" -> ")[1])
		diff = ast.literal_eval(splitted[1].replace("diff=array(", "").replace(")", ""))
		mapping = ast.literal_eval(splitted[2].replace("mapping=", ""))
		instructions.append([
			scanner_from,
			scanner_to,
			diff,
			mapping
			])
	
	for inst in reversed(instructions):
		scanner_from = scanners[inst[0]]
		scanner_to = scanners[inst[1]]
		diff = inst[2]
		mapping = inst[3]

		scanner_from_trans_diff = transform(scanner_from, mapping) - diff
		scanners[inst[1]] = np.vstack((scanner_to,scanner_from_trans_diff))
	unique_scanner0 = np.unique(scanners[0], axis=0)

	max_manhattan_distance = 0
	for idx, scanner1 in enumerate(unique_scanner0):
		for scanner2 in unique_scanner0[idx+1:]:
			manhattan_distance = np.abs(scanner1 - scanner2).sum()
			max_manhattan_distance = max(max_manhattan_distance, manhattan_distance)
	print(max_manhattan_distance)


def transform(scanner, mapping):
	new_scanner = deepcopy(scanner)
	for axis in range(3):
		new_scanner[:,axis] = scanner[:,mapping[axis][0]] * mapping[axis][1]
	return new_scanner[np.lexsort((new_scanner[:,2], new_scanner[:,1],new_scanner[:,0]))][::-1]

#main("example.txt")
main("input.txt")
