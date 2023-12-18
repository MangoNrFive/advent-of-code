import numpy as np


with open('input2.txt') as f:
	lines = f.readlines()

col_pos = np.iinfo(np.int32).max//2 + 1
area = 1
for line in lines:
	_, _, COLOR = line.strip().replace("(", "").replace(")", "").replace("#", "").split(" ")
	DIRECTION = COLOR[-1]
	LENGTH = int(COLOR[:-1], 16)

	area += LENGTH
	if DIRECTION == "0":
		col_pos += LENGTH
	elif DIRECTION == "1":
		area += (col_pos + 1) * LENGTH
	elif DIRECTION == "2":
		col_pos -= LENGTH
		area -= LENGTH
	elif DIRECTION == "3":
		area -= (col_pos + 2) * LENGTH
	else:
		ValueError("unknown direction")

print(area)
