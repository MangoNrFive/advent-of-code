import re
import math


with open('input3.txt') as f:
    INSTRUCTIONS_CHAR = next(f).strip()
    next(f)
    lines = f.readlines()

INSTRUCTIONS = [0 if i == "L" else 1 for i in INSTRUCTIONS_CHAR]

NODES = {}
START_POSS = []
for line in lines:
    i, nl, nr = re.findall(r"[0-9A-Z]{3}", line)
    NODES[i] = (nl, nr)
    if i[2] == "A":
        START_POSS.append(i)


def get_cycles(nodes, instructions, start_pos):
    visited = []
    ends = []
    pos = start_pos

    idx = 0
    while True:
        for instruction_idx, instruction in enumerate(instructions):
            if pos[2] == "Z":
                ends.append(idx)

            visit = (instruction_idx, pos)
            if visit in visited:
                len_cycle = idx - visited.index(visit)
                return len_cycle
            else:
                visited.append(visit)

            path = nodes[pos]
            pos = path[instruction]

            idx += 1


len_cycles = []
for START_POS in START_POSS:
    len_cycles.append(get_cycles(NODES, INSTRUCTIONS, START_POS))

print(math.lcm(*len_cycles))
