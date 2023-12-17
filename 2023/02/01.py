import re


with open('input2.txt') as f:
	lines = f.readlines()

ALLOWED = {
	"red": 12,
	"green": 13,
	"blue": 14,
}

sum_valid_IDs = 0
for id_0, line in enumerate(lines):
	_, DRAWS = line.strip().replace(" ", "").split(":")
	valid = True
	for DRAW in DRAWS.split(";"):
		for BATCH in DRAW.split(","):
			num = int(re.search(r'\d+', BATCH).group())
			color = re.sub(r'\d+', '', BATCH)
			if num > ALLOWED[color]:
				valid = False
	if valid:
		sum_valid_IDs += id_0+1

print(sum_valid_IDs)
