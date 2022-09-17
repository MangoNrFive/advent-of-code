import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import ast
from copy import deepcopy


#TODO deepcopy in function and return copy
def main(file):
	with open(file) as f:
		lines = f.readlines()
	numbers = [ast.literal_eval(number.replace("\n", "")) for number in lines]

	max_magnitude = 0
	for idx1, number1 in enumerate(deepcopy(numbers)):
		for idx2, number2 in enumerate(deepcopy(numbers)):
			if idx1 != idx2:
				number_sum = add(deepcopy(number1), deepcopy(number2))
				number_sum = reduce(number_sum)
				new_magnitude = magnitude(number_sum)
				if new_magnitude > max_magnitude:
					max_magnitude = new_magnitude
	print(max_magnitude)


def crawl(numbers, idx):
	for local_idx, number in enumerate(numbers):
		if isinstance(number, int):
			yield number, idx + [local_idx]
		else:
			for num, i in crawl(number, idx + [local_idx]):
				yield num, i

def nested_set(nlist, index, value):
    if isinstance(index, int):
        nlist[index] = value
        return
    elif len(index) == 1:
        nlist[index[0]] = value
        return
    nested_set(nlist[index[0]], index[1:], value)


def add(number_1, number_2):
	return [number_1, number_2]


def reduce(number):
	splitted = True
	while splitted:
		exploded = True
		while exploded:
			number, exploded = explode(number)
		number, splitted = split(number)
	return number


def explode(numbers):
	last_number = None
	last_idx = None
	iterator = crawl(numbers, [])
	for number, idx in iterator:
		if len(idx) > 4:
			if last_number is not None:
				nested_set(numbers, last_idx, last_number+number)
			try:
				number2, _ = next(iterator)
				next_number, next_idx = next(iterator)
			except StopIteration:
				pass
			else:
				nested_set(numbers, next_idx, next_number+number2)

			nested_set(numbers, idx[:-1], 0)
			return numbers, True

		last_number = number
		last_idx = idx		

	return numbers, False


def split(numbers):
	for number, idx in crawl(numbers, []):
		if number > 9:
			nested_set(numbers, idx, [math.floor(number/2), math.ceil(number/2)])
			return numbers, True
	return numbers, False


def magnitude(numbers):
	if isinstance(numbers, int):
		return numbers
	else:
		return 3*magnitude(numbers[0]) + 2*magnitude(numbers[1])



main("example_5.txt")
main("input.txt")
