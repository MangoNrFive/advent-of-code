with open('input2.txt') as f:
	lines = f.readlines()

SPRINGS = []
for line in lines:
	s, a = line.strip().split()
	SPRINGS.append((s, [int(e) for e in a.split(",")]))


def get_variant_counts(string, clusters_left):
	if len(clusters_left) == 0:
		return 1

	variant_counts = 0
	maximum_shift = len(string) - sum(clusters_left) - len(clusters_left) + 1
	for shift in range(maximum_shift + 1):
		if (
				"#" not in string[:shift]  # no springs in front of arrangement
				and "." not in string[shift:shift + clusters_left[0]]  # no holes in arrangement
				and (shift + clusters_left[0] >= len(string) or not "#" == string[shift + clusters_left[0]])  # no spring directly after arrangement
				and (len(clusters_left) > 1 or "#" not in string[shift + clusters_left[0]:])  # no spring after if last arrangement
		):
			variant_counts += get_variant_counts(string[shift + clusters_left[0] + 1:], clusters_left[1:])
	return variant_counts


res = sum(get_variant_counts(*SPRING) for SPRING in SPRINGS)
print(res)
