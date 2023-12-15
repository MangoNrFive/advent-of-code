import numpy as np


with open('input1.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append(list(line.strip()))
FIELD = np.array(FIELD)


movements = 0
pos = np.where(FIELD == "S")
p_r = pos[0][0]
p_c = pos[1][0]

# input 1
#v_r = 0
#v_c = 1

# input 2
v_r = 1
v_c = 0

while True:
	movements += 1
	p_r += v_r
	p_c += v_c
	pipe = FIELD[p_r, p_c]
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

print(movements / 2)
