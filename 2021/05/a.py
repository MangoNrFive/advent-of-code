import numpy as np
import math


def main(file):
	with open(file) as f:
		lines = f.readlines()

	arr = []
	for line in lines:
		arr.append(line.replace("\n", "").replace(" -> ", ","))


	x1 = [int(element.split(",")[0]) for element in arr]
	y1 = [int(element.split(",")[1]) for element in arr]
	x2 = [int(element.split(",")[2]) for element in arr]
	y2 = [int(element.split(",")[3]) for element in arr]

	overlaps = np.zeros((max(x1 + x2)+1, max(y1 + y2)+1))

	for x1_i, y1_i, x2_i, y2_i in zip(x1, y1, x2, y2):
		if x1_i == x2_i:
			overlaps[x1_i, min(y1_i, y2_i):max(y1_i, y2_i)+1] += 1
		elif y1_i == y2_i:
			overlaps[min(x1_i, x2_i):max(x1_i, x2_i)+1, y1_i] += 1
		else:
			if x1_i > x2_i:
				xstep = -1
			else:
				xstep = 1
			if y1_i > y2_i:
				ystep = -1
			else:
				ystep = 1
			print("#####################")
			print(overlaps.transpose())
			print(f"line: {x1_i,y1_i} -> {x2_i,y2_i}")
			for x_id, y_id in zip(range(x1_i, x2_i+xstep, xstep), range(y1_i, y2_i+ystep, ystep)):
				overlaps[x_id, y_id] += 1
			print(overlaps.transpose())
	print(overlaps.transpose())

	print((overlaps>1).sum())



main("example.txt")
main("input.txt")
