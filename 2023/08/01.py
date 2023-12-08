import re


with open('input3.txt') as f:
	INSTRUCTIONS = next(f)
	next(f)
	lines = f.readlines()

NODES = {}
for line in lines:
	i, nl, nr = re.findall(r"[A-Z]{3}", line)
	NODES[i] = (nl, nr)


def get_steps(instructions, nodes):
	pos = "AAA"
	steps = 1
	while True:
		for instruction in instructions:
			path = nodes[pos]
			if instruction == "R":
				pos = path[1]
			elif instruction == "L":
				pos = path[0]
			else:
				continue
			if pos == "ZZZ":
				return steps
			steps += 1


print(get_steps(INSTRUCTIONS, NODES))
