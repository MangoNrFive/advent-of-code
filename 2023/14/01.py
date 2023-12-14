with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append(line.strip())

total_load = 0
FIELD_tilted = []
for column in map(list, zip(*FIELD)):
	column_tilted = []
	sub_column_tilted = []
	for element in column:
		if element == "#":
			column_tilted += sub_column_tilted
			sub_column_tilted = []
			column_tilted.append("#")
		elif element == "O":
			sub_column_tilted.insert(0, "O")
		elif element == ".":
			sub_column_tilted.append(".")
	column_tilted += sub_column_tilted
	FIELD_tilted.append(column_tilted)
	total_load += sum(idx+1 if element == "O" else 0 for idx, element in enumerate(reversed(column_tilted)))

print(total_load)
