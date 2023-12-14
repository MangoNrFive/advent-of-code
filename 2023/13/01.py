import numpy as np


with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
FIELDS = []
for line in lines:
	if line == "\n":
		FIELDS.append(np.array(FIELD, dtype=np.int32))
		FIELD = []
		continue
	FIELD.append(list(line.strip().replace(".", "0").replace("#", "1")))
FIELDS.append(np.array(FIELD, dtype=np.int32))


def find_symmetry(array):
	for axis in (0, 1):
		len_axis = array.shape[axis]

		for i in range(1, len_axis):
			len_mirrored = min(i, len_axis-i)
			if np.array_equal(array.take(indices=range(i-len_mirrored, i+len_mirrored), axis=axis), np.flip(array.take(indices=range(i-len_mirrored, i+len_mirrored), axis=axis), axis)):
				return i if axis else 100*i


print(sum(find_symmetry(FIELD) for FIELD in FIELDS))
