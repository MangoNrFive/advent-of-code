with open('input2.txt') as f:
	lines = f.readlines()


def aoc_hash(string):
	current_value = 0
	for char in string:
		current_value += ord(char)
		current_value *= 17
		current_value %= 256
	return current_value


res = sum(aoc_hash(string) for string in lines[0].strip().split(","))
print(res)
