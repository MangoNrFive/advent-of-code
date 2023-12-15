import numpy as np


with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append(list(line.strip()))
FIELD = np.array(FIELD)

FIELD_PATH = np.full_like(FIELD, ".")

movements = 0
pos = np.where(FIELD == "S")
p_r = pos[0][0]
p_c = pos[1][0]

# input 1
#v_r = 0
#v_c = 1
#startpipe = "F"

# input 2
v_r = 1
v_c = 0
startpipe = "|"

while True:
	movements += 1
	p_r += v_r
	p_c += v_c
	pipe = FIELD[p_r, p_c]
	FIELD_PATH[p_r, p_c] = pipe
	if pipe in ["|", "-"]:
		pass
	elif pipe in ["F", "J"]:
		v_c, v_r = -v_r, -v_c
	elif pipe in ["L", "7"]:
		v_c, v_r = v_r, v_c
	elif pipe == "S":
		break
	elif pipe == ".":
		raise ValueError("no pipe")
	else:
		raise ValueError("unknown pipe")


FIELD_PATH[p_r, p_c] = startpipe
print(FIELD_PATH)

enclosed = 0
for row in FIELD_PATH:
	inside = 0
	wall = 0
	for element in row:
		if element == "|":
			inside = 1 - inside
		elif element == "-":
			pass
		elif element in ["F", "J"]:
			wall += 0.5
		elif element in ["L", "7"]:
			wall -= 0.5
		elif element == "." and inside:
			enclosed += 1

		if abs(wall) == 1:
			inside = 1 - inside
			wall = 0

print(enclosed)
