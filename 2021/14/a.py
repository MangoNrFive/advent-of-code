import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter


arr = []
def main(file, steps):
	with open(file) as f:
		lines = f.readlines()
		joind_lines = "".join(lines)

	joind_lines = "".join(lines)
	polymer = joind_lines.split("\n\n")[0]
	raw_polymerization = joind_lines.split("\n\n")[1]

	polymerization = [(poly.split(" -> ")[0], poly.split(" -> ")[1]) for poly in raw_polymerization.split("\n")]


	for step in range(steps):
		for pre_poly, post_poly in polymerization:
			old_polymer = ""
			while polymer != old_polymer:
				old_polymer = polymer
				new_poly = pre_poly[0] + post_poly.lower() + pre_poly[1]
				polymer = polymer.replace(pre_poly, new_poly)
		polymer = polymer.upper()

	counts = Counter(polymer)
	print(counts)


main("example.txt", 40)
main("input.txt", 40)
