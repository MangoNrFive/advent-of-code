import numpy as np


with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append([char if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."] else "#" for char in line.strip()])
FIELD = np.array(FIELD)
FIELD = np.pad(FIELD, [(2, 2), (2, 2)], mode='constant', constant_values=".")

total_part_num = 0
for row_idx, row in enumerate(FIELD[1:-1]):
	number = []
	for col_idx, element in enumerate(row[1:-1]):
		if element.isdigit():
			number.append(element)
		else:
			if number:
				if "#" in FIELD[row_idx:row_idx+3, col_idx-len(number):col_idx+2]:
					total_part_num += int("".join(number))
				number = []

print(total_part_num)
