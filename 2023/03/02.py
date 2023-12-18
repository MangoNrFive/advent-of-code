import numpy as np


with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append([char if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "*"] else "." for char in line.strip()])
FIELD = np.array(FIELD)
FIELD = np.pad(FIELD, [(2, 2), (2, 2)], mode='constant', constant_values=".")

gears = {}
for row_idx, row in enumerate(FIELD[1:-1]):
	number = []
	for col_idx, element in enumerate(row[1:-1]):
		if element.isdigit():
			number.append(element)
		else:
			if number:
				sub_field = FIELD[row_idx:row_idx+3, col_idx-len(number):col_idx+2]
				if "*" in sub_field:
					for sub_row_star, sub_col_star in zip(*np.where(sub_field == "*")):
						gear_idx = (row_idx+sub_row_star, col_idx+sub_col_star-len(number))
						if gear_idx in gears:
							gears[gear_idx].append(int("".join(number)))
						else:
							gears[gear_idx] = [int("".join(number))]
				number = []

total_gear_ratio = 0
for numbers in gears.values():
	if len(numbers) == 2:
		total_gear_ratio += numbers[0] * numbers[1]

print(total_gear_ratio)
