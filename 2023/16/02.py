from dataclasses import dataclass
import numpy as np


with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append(list(line.strip()))
FIELD = np.array(FIELD)


@dataclass
class Beam:
	v_row: int
	v_col: int
	row: int
	col: int


def find_energized(start_beam):
	visited = {
		(-1, 0): np.full_like(FIELD, False, dtype=bool),  # north
		(0, 1): np.full_like(FIELD, False, dtype=bool),  # east
		(1, 0): np.full_like(FIELD, False, dtype=bool),  # south
		(0, -1): np.full_like(FIELD, False, dtype=bool),  # west
	}

	beams = [start_beam]

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
	return np.sum(any_visited)


max_energized = 0
rows, cols = FIELD.shape

for row in range(rows):
	start_beam = Beam(0, 1, row, 0)
	max_energized = max(max_energized, find_energized(start_beam))

for row in range(rows):
	start_beam = Beam(0, -1, row, cols)
	max_energized = max(max_energized, find_energized(start_beam))

for col in range(cols):
	start_beam = Beam(1, 0, 0, col)
	max_energized = max(max_energized, find_energized(start_beam))

for col in range(cols):
	start_beam = Beam(-1, 0, rows, col)
	max_energized = max(max_energized, find_energized(start_beam))

print(max_energized)
