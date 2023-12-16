from dataclasses import dataclass
import numpy as np


with open('input1.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append(list(line.strip()))
FIELD = np.array(FIELD)

visited = {
	(-1, 0): np.full_like(FIELD, False, dtype=bool),  # north
	(0, 1): np.full_like(FIELD, False, dtype=bool),  # east
	(1, 0): np.full_like(FIELD, False, dtype=bool),  # south
	(0, -1): np.full_like(FIELD, False, dtype=bool),  # west
}


@dataclass
class Beam:
	v_row: int
	v_col: int
	row: int
	col: int


beams = [Beam(0, 1, 0, 0)]

while beams:
	beam = beams[0]

	# check if inside Field else delete beam
	if not 0 <= beam.row < FIELD.shape[0] or not 0 <= beam.col < FIELD.shape[1]:
		beams.pop(0)
		continue

	# set visited, delete if already visited in this direction
	direction = (beam.v_row, beam.v_col)
	if visited[direction][beam.row, beam.col]:
		beams.pop(0)
		continue
	else:
		visited[direction][beam.row, beam.col] = True

	# change direction
	tile = FIELD[beam.row, beam.col]
	if (tile == "."
		or tile == "|" and not beam.v_col
		or tile == "-" and not beam.v_row
	):
		pass
	elif tile == "\\":
		beam.v_row, beam.v_col = beam.v_col, beam.v_row
	elif tile == "/":
		beam.v_row, beam.v_col = -beam.v_col, -beam.v_row
	elif (tile == "."
			or tile == "|" and beam.v_col
			or tile == "-" and beam.v_row
	):
		beams.append(Beam(beam.v_col, beam.v_row, beam.row, beam.col))
		beam.v_row, beam.v_col = -beam.v_col, -beam.v_row
	else:
		raise ValueError("unknown tile")

	# move
	beam.row += beam.v_row
	beam.col += beam.v_col

any_visited = np.logical_or(np.logical_or(np.logical_or(visited[(-1, 0)], visited[(0, 1)]), visited[(1, 0)]), visited[(0, -1)])
print(np.sum(any_visited))
