import numpy as np

with open('input2.txt') as f:
	lines = f.readlines()

field = []
for line in lines:
	field.append(list(line.strip()))
field = np.array(field)

field = np.pad(field, [(1, 1), (1, 1)], mode='constant', constant_values=".")
field = np.char.replace(field, "S", "O")

FIELD_ROCKS = np.char.replace(field, "O", ".")

row_count, col_count = field.shape
for _ in range(64):
	new_field = FIELD_ROCKS.copy()
	for r in range(1, row_count - 1):
		for c in range(1, col_count - 1):
			if not FIELD_ROCKS[r, c] == "#" and (field[r + 1, c] == "O"
					or field[r, c + 1] == "O"
					or field[r - 1, c] == "O"
					or field[r, c - 1] == "O"):
				new_field[r, c] = "O"
	field = new_field.copy()

print(np.sum(field == "O"))
