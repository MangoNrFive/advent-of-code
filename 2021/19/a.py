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
	scanners = [np.array([(int(e.split(",")[0]), int(e.split(",")[1]), int(e.split(",")[2])) for e in joined_line.split("\n")[1:]]) for joined_line in joined_lines.split("\n\n")]
	scanners = [(idx, a[np.lexsort((a[:,2], a[:,1],a[:,0]))][::-1]) for idx, a in enumerate(scanners)]

	scanners_joined = [deepcopy(scanners[0])]
	scanners_solo = deepcopy(scanners[1:])
	while True:
		for scanner1 in scanners_joined:
			if not len(scanners_solo):
				return
			for idx2, scanner2 in enumerate(scanners_solo):
				for mapping in MAPPINGS:
					diff = find_overlapping(scanner1[1], transform(scanner2[1], mapping))
					if diff is not None:
						print(f"scanner{scanner2[0]} -> scanner{scanner1[0]}")
						print(f"{diff=}")
						print(f"{mapping=}")
						print("\n")
						scanners_joined.append(scanner2)
						del scanners_solo[idx2]
						break
					else:
						continue
					break
				else:
					continue
				break
			else:
				continue
			break


def find_overlapping(scanner1, scanner2):
	len_scanner1 = len(scanner1)
	for idx1, beacon1 in enumerate(scanner1[:-11]):
		for idx2, beacon2 in enumerate(scanner2[:-11]):
			diff = beacon2 - beacon1
			matches = 1
			didx=0
			for midx1, beacon1_m in enumerate(scanner1[idx1+1:]):
				for midx2, beacon2_m in enumerate(scanner2[idx2+didx+1:matches-11 or None]):
					if (beacon2_m - beacon1_m == diff).all():
						if matches >= 11:
							return diff
						matches += 1
						didx += midx2 + 1
						break
				if len_scanner1 - (idx1+1) - (midx1+1) < 12 - matches:
					break


def transform(scanner, mapping):
	new_scanner = deepcopy(scanner)
	for axis in range(3):
		new_scanner[:,axis] = scanner[:,mapping[axis][0]] * mapping[axis][1]
	return new_scanner[np.lexsort((new_scanner[:,2], new_scanner[:,1],new_scanner[:,0]))][::-1]

#main("example.txt")
main("input.txt")
