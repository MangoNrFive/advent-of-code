import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter


version_sum = None


def main(file):
	with open(file) as f:
		target_coords = f.readlines()[0].replace("target area: ", "").split(", ")
	target_x_str = target_coords[0].replace("x=", "").split("..")
	target_y_str = target_coords[1].replace("y=", "").split("..")

	t_x_l = int(target_x_str[0])
	t_x_r = int(target_x_str[1])
	t_y_d = int(target_y_str[0])
	t_y_u = int(target_y_str[1])

	goals = []
	for v_y_start in range(-1*t_y_d, t_y_d-1, -1):
		steps = 0
		v_y = v_y_start
		y = 0

		while y >= t_y_d:
			y += v_y
			v_y -= 1
			steps += 1
			if t_y_d <= y <= t_y_u:
				for v_x_start in range(t_x_r+1):
					v_x = v_x_start
					x = 0
					for step in range(steps):
						x += v_x
						v_x = max(0, v_x-1)
					if t_x_l <= x <= t_x_r:
						goals.append((v_x_start, v_y_start))


	print(len(set(goals)))

main("example.txt")
main("input.txt")
