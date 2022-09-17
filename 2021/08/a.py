import numpy as np
import math


def main(file):
	with open(file) as f:
		lines = f.readlines()

	input_list = [element.replace("\n", "").split(" | ")[0].split() for element in lines]
	output_list = [element.replace("\n", "").split(" | ")[1].split() for element in lines]

	numbers = []
	for input_i, output_i in zip(input_list, output_list):
		one = [element for element in input_i if len(element) == 2][0]
		four = [element for element in input_i if len(element) == 4][0]
		seven = [element for element in input_i if len(element) == 3][0]

		characters = "abcdefg"
		counts = [".".join(input_i).count(char) for char in characters]

		real_segments = [None]*7
		for idx, count in enumerate(counts):
			if count == 4:
				real_segments[idx] = "E"
			elif count == 6:
				real_segments[idx] = "B"
			elif count == 7:
				char = characters[idx]
				if char in four and char not in one:
					real_segments[idx] = "D"
				else:
					real_segments[idx] = "G"
			elif count == 8:
				char = characters[idx]
				if char in seven and char not in one:
					real_segments[idx] = "A"
				else:
					real_segments[idx] = "C"
			elif count == 9:
				real_segments[idx] = "F"
			else:
				raise Exception


		digits = []
		for output_ii in output_i:
			output_ii_decoded = output_ii[:]
			for char, real in zip(characters, real_segments):
				output_ii_decoded = output_ii_decoded.replace(char, real)

			compare_str = "".join(sorted(output_ii_decoded))
			if compare_str == "ABCEFG":
				digits.append("0")
			elif compare_str == "CF":
				digits.append("1")
			elif compare_str == "ACDEG":
				digits.append("2")
			elif compare_str == "ACDFG":
				digits.append("3")
			elif compare_str == "BCDF":
				digits.append("4")
			elif compare_str == "ABDFG":
				digits.append("5")
			elif compare_str == "ABDEFG":
				digits.append("6")
			elif compare_str == "ACF":
				digits.append("7")
			elif compare_str == "ABCDEFG":
				digits.append("8")
			elif compare_str == "ABCDFG":
				digits.append("9")
			else:
				raise Exception
		number = int("".join(digits))
		numbers.append(number)
	print(sum(numbers))


main("example.txt")
main("input.txt")
