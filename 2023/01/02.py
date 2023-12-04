import re


nums = {
	"one": "1",
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9",
}


def convert_to_num(matched):
	print(matched)
	return int(nums.get(matched[0], matched[0]) + nums.get(matched[-1], matched[-1]))


with open('input2.txt') as f:
	lines = f.readlines()

arr = []
for line in lines:
	arr.append(line)

res = sum(convert_to_num(re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', row)) for row in arr)
print(res)
