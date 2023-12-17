import re
import math


with open('input2.txt') as f:
	lines = f.readlines()

sum_power = 0
for id_0, line in enumerate(lines):
	_, DRAWS = line.strip().replace(" ", "").split(":")
	minimum = {
		"red": 0,
		"green": 0,
		"blue": 0,
	}
	for DRAW in DRAWS.split(";"):
		for BATCH in DRAW.split(","):
			num = int(re.search(r'\d+', BATCH).group())
			color = re.sub(r'\d+', '', BATCH)
			minimum[color] = max(minimum[color], num)
	sum_power += math.prod(minimum.values())

print(sum_power)
