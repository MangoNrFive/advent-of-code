with open('input2.txt') as f:
	lines = f.readlines()


def aoc_hash(string):
	current_value = 0
	for char in string:
		current_value += ord(char)
		current_value *= 17
		current_value %= 256
	return current_value


hashmap = [dict() for _ in range(256)]
for STEP in list(lines[0].strip().split(",")):
	if "-" in STEP:
		label = STEP.strip("-")
		label_hash = int(aoc_hash(label))
		hashmap[label_hash].pop(label, None)
	if "=" in STEP:
		label, focal_length = STEP.split("=")
		label_hash = int(aoc_hash(label))
		hashmap[label_hash][label] = int(focal_length)


def focusing_power(box):
	return sum((idx+1)*fl for idx, fl in enumerate(box.values()))


res = sum((idx+1)*focusing_power(box) for idx, box in enumerate(hashmap))
print(res)
