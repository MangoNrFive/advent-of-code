import re


with open('input2.txt') as f:
	lines = f.readlines()

points = 0
for line in lines:
	w, s = line.strip().split(":")[1].replace("  ", " ").split("|")
	winning = [int(num) for num in re.findall(r'\d+', w)]
	selecteds = [int(num) for num in re.findall(r'\d+', s)]

	selected_winners = 0
	for selected in selecteds:
		if selected in winning:
			selected_winners += 1

	if selected_winners:
		points += 2**(selected_winners - 1)

print(points)
