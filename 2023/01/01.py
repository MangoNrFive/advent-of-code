import re


with open('input2.txt') as f:
	lines = f.readlines()

arr = []
for line in lines:
	arr.append(line)

res = sum(int(re.search(r'(\d{1})', row).group() + re.search(r'(\d{1})', row[::-1]).group()) for row in arr)
print(res)
