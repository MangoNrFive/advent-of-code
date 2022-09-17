import numpy as np
import math


def main(file):
	with open(file) as f:
		lines = f.readlines()

	arr = []
	for line in lines:
		arr.append(line.replace("\n", ""))


	o = arr[:]
	c = arr[:]
	for idx in range(len(arr[0])):
		o_1 = [element for element in o if element[idx] == "1"]
		o_0 = [element for element in o if element[idx] == "0"]

		if len(o_1) >= len(o_0):
			o = o_1[:]
		else:
			o = o_0[:]

		if len(o) == 1:
			oxygen = o[0]

		c_1 = [element for element in c if element[idx] == "1"]
		c_0 = [element for element in c if element[idx] == "0"]

		if len(c_1) < len(c_0):
			c = c_1[:]
		else:
			c = c_0[:]

		if len(c) == 1:
			co2 = c[0]

	print(int(oxygen, 2) * int(co2, 2))




main("example.txt")
main("input.txt")
