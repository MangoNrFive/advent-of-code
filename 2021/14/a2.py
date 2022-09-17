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
	template = joind_lines.split("\n\n")[0]
	raw_polymerization = joind_lines.split("\n\n")[1]

	polymerization_map = {poly.split(" -> ")[0]: (poly.split(" -> ")[0][0] + poly.split(" -> ")[1], poly.split(" -> ")[1] + poly.split(" -> ")[0][1]) for poly in raw_polymerization.split("\n")}

	polymers = defaultdict(int)
	for char_pair in range(len(template) - 1):
		polymers[template[char_pair:char_pair+2]] += 1

	for step in range(steps):
		old_polymers = polymers.copy()
		for poly_key, poly_value in old_polymers.items():
			if poly_value:
				new_1 = polymerization_map[poly_key][0]
				new_2 = polymerization_map[poly_key][1]

				polymers[new_1] += poly_value
				polymers[new_2] += poly_value
				polymers[poly_key] -= poly_value

	char_counts = defaultdict(float)
	for poly_key, poly_value in polymers.items():
		char_counts[poly_key[0]] += poly_value / 2
		char_counts[poly_key[1]] += poly_value / 2

	char_counts[template[0]] += 0.5
	char_counts[template[-1]] += 0.5

	for key, value in char_counts.items():
		print(f"{key}: {value}")


#main("example.txt", 40)
main("input.txt", 40)
