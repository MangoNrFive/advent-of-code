from functools import partial
import numpy as np


with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append(list(line.strip().replace("O", "1").replace(".", "0").replace("#", "2")))
field = np.array(FIELD, dtype=np.int32)


def tilt_column(column, reverse=False):
	if reverse:
		column = reversed(column)
	column_tilted = []
	sub_column_tilted = []
	for element in column:
		if element == 2:
			column_tilted += sub_column_tilted
			sub_column_tilted = []
			column_tilted.append(2)
		elif element == 1:
			sub_column_tilted.insert(0, 1)
		elif element == 0:
			sub_column_tilted.append(0)
	if reverse:
		return list(reversed(column_tilted + sub_column_tilted))
	return column_tilted + sub_column_tilted


tilt_column_reversed = partial(tilt_column, reverse=True)

seen = {}
cycles = 1000000000
i = 0
cut = False
while i < cycles:
	field = np.apply_along_axis(tilt_column, 0, field)  # north
	field = np.apply_along_axis(tilt_column, 1, field)  # west
	field = np.apply_along_axis(tilt_column_reversed, 0, field)  # south
	field = np.apply_along_axis(tilt_column_reversed, 1, field)  # east
	if i > 100 and not cut:
		if np.array2string(field, max_line_width=np.inf, threshold=np.inf) in seen:
			cut = True
			cycle_len = i - seen[np.array2string(field, max_line_width=np.inf, threshold=np.inf)]
			cycles_left = cycles - i
			cycles = cycles_left % cycle_len + i
		else:
			seen[np.array2string(field, max_line_width=np.inf, threshold=np.inf)] = i
	i += 1


def calculate_load(column):
	return sum(idx + 1 if element == 1 else 0 for idx, element in enumerate(reversed(column)))


print(sum(np.apply_along_axis(calculate_load, 0, field)))
