import numpy as np
import math


def main(file, days):
	with open(file) as f:
		lines = f.readlines()

	timers = [int(element) for element in lines[0].split(",")]

	age_counts = [0]*9

	for timer in timers:
		age_counts[timer] += 1

	for day in range(days):
		age_counts_old = age_counts[:]
		age_counts = age_counts_old[1:] + [age_counts_old[0]]
		age_counts[6] += age_counts_old[0]
	print(sum(age_counts))

#main("example.txt", 256)
main("input.txt", 256)
