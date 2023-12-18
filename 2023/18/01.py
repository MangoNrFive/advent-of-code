import numpy as np
from scipy.ndimage import label


with open('input2.txt') as f:
	lines = f.readlines()

SCALE = 500
row_pos = SCALE
col_pos = SCALE
field = np.array([[0]])
field = np.pad(field, [(SCALE, SCALE), (SCALE, SCALE)], mode='constant', constant_values=1)

for line in lines:
	DIRECTION, LENGTH, COLOR = line.strip().replace("(", "").replace(")", "").replace("#", "").split(" ")
	LENGTH = int(LENGTH)

	if DIRECTION == "U":
		field[row_pos - LENGTH:row_pos, col_pos] = [0]*LENGTH
		row_pos -= LENGTH
	elif DIRECTION == "R":
		field[row_pos, col_pos + 1:col_pos + LENGTH + 1] = [0]*LENGTH
		col_pos += LENGTH
	elif DIRECTION == "D":
		field[row_pos + 1: row_pos + LENGTH + 1, col_pos] = [0]*LENGTH
		row_pos += LENGTH
	elif DIRECTION == "L":
		field[row_pos, col_pos - LENGTH:col_pos] = [0]*LENGTH
		col_pos -= LENGTH
	else:
		ValueError("unknown direction")


labeled_field, _ = label(field)
print(f"border: {np.sum(labeled_field == 0)}")
print(f"inside: {np.sum(labeled_field == 2)}")
print(f"total: {np.sum(labeled_field == 0) + np.sum(labeled_field == 2)}")
