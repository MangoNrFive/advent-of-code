import math
import numpy as np


STEPS = 26501365

with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append(list(line.strip()))
FIELD = np.array(FIELD)

ROW_NUM, COL_NUM = FIELD.shape
if not ROW_NUM == COL_NUM:
	raise ValueError("algorithm only works on quadratic array")
NUM = ROW_NUM

if "#" in FIELD[NUM//2, :] or "#" in FIELD[:, NUM//2]:
	raise ValueError("algorithm only works if there are no rocks in column or row of starting-position")

FIELD_ROCKS = np.pad(FIELD, [(1, 1), (1, 1)], mode='constant', constant_values=".")
FIELD_ROCKS = np.char.replace(FIELD_ROCKS, "S", ".")

full_tiles_in_between_straight, steps_straight = divmod(STEPS - NUM//2 - 1, NUM)


def get_full_tiles(num_tiles_straight):
	if num_tiles_straight == 0:
		return 0, 1
	i_odd = math.ceil(num_tiles_straight / 2) * 2
	odd = i_odd**2

	i_even = math.ceil((num_tiles_straight-1) / 2) * 2
	even = i_even**2 + 2*i_even + 1
	return odd, even


steps_diagonal_outer = (STEPS - NUM//2 * 2 - 2) % NUM
steps_diagonal_inner = steps_diagonal_outer + NUM
tiles_full_odd, tiles_full_even = get_full_tiles(full_tiles_in_between_straight)


tiles_diagonal_outer = full_tiles_in_between_straight + 1
tiles_diagonal_inner = full_tiles_in_between_straight

PARTIAL_TILES = [
	(NUM//2, NUM//2, tiles_full_even, NUM*2+STEPS%2),
	(NUM//2, NUM//2, tiles_full_odd, NUM*2+STEPS%2 + 1),
	(NUM//2, 0, 1, steps_straight),
	(0, NUM//2, 1, steps_straight),
	(NUM//2, -1, 1, steps_straight),
	(-1, NUM//2, 1, steps_straight),
	(0, 0, tiles_diagonal_outer, steps_diagonal_outer),
	(0, -1, tiles_diagonal_outer, steps_diagonal_outer),
	(-1, 0, tiles_diagonal_outer, steps_diagonal_outer),
	(-1, -1, tiles_diagonal_outer, steps_diagonal_outer),
	(0, 0, tiles_diagonal_inner, steps_diagonal_inner),
	(0, -1, tiles_diagonal_inner, steps_diagonal_inner),
	(-1, 0, tiles_diagonal_inner, steps_diagonal_inner),
	(-1, -1, tiles_diagonal_inner, steps_diagonal_inner),
]


def find_reachable(s_row, s_col, i):
	if s_row == -1:
		s_row = -2
	else:
		s_row += 1

	if s_col == -1:
		s_col = -2
	else:
		s_col += 1

	field = FIELD_ROCKS.copy()
	field[s_row, s_col] = "O"
	for _ in range(i):
		new_field = FIELD_ROCKS.copy()
		for r in range(1, NUM+1):
			for c in range(1, NUM+1):
				if not FIELD_ROCKS[r, c] == "#" and (field[r + 1, c] == "O"
						or field[r, c + 1] == "O"
						or field[r - 1, c] == "O"
						or field[r, c - 1] == "O"):
					new_field[r, c] = "O"
		field = new_field.copy()
	return np.sum(field == "O")


# partial tiles
garden_plots_reached = 0
for start_row, start_col, number_of_tiles, steps_left in PARTIAL_TILES:
	garden_plots_reached += find_reachable(start_row, start_col, steps_left) * number_of_tiles

print(garden_plots_reached)
