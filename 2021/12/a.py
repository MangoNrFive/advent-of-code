import numpy as np
import math
from statistics import median
from collections import defaultdict


arr = []
def main(file):
	with open(file) as f:
		lines = f.readlines()

	arr = [(line.replace("\n", "").split("-")[0], line.replace("\n", "").split("-")[1]) for line in lines]

	CAVES = defaultdict(list)
	for element_1, element_2 in arr:
		CAVES[element_1].append(element_2)
		CAVES[element_2].append(element_1)

	paths = crawl(CAVES, "start", [])

	print(len(paths))

def crawl(CAVES, current_node, path):
	paths = []

	options = CAVES[current_node]
	for option in options:
		if option == "end":
			paths.append(path + [current_node, option])
		elif option.islower() and option in path:
			pass
		else:
			crawled = crawl(CAVES, option, path + [current_node])
			for path_crawled in crawled:
				paths.append(path_crawled)
	return paths


#main("example1.txt")
#main("example2.txt")
#main("example3.txt")
main("input.txt")
