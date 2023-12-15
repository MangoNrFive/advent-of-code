def get_minimum_sizes(string, clusters):
	r_string = string[::-1]
	r_clusters = clusters[::-1]
	r_minimum_sizes = []
	minimum_size = 0
	for r_cluster in r_clusters:
		shift = 0
		while "." in r_string[shift:shift+r_cluster] or (shift+r_cluster < len(r_string) and r_string[shift+r_cluster] == "#"):
			shift += 1

		minimum_size += r_cluster
		minimum_size += shift
		r_minimum_sizes.append(minimum_size)
		r_string = r_string[shift+r_cluster+1:]
		minimum_size += 1

	return r_minimum_sizes[::-1]


with open('input1.txt') as f:
	lines = f.readlines()

SPRINGS = []
for line in lines:
	s, a = line.strip().split()
	#s = ",".join([s]*5)
	#a = ",".join([a]*5)
	a = [int(e) for e in a.split(",")]
	m = get_minimum_sizes(s, a)
	SPRINGS.append((s, a, m))


def get_variant_counts(string, clusters_left, minimum_sizes):
	if len(clusters_left) == 0:
		return 1

	len_cluster = clusters_left[0]
	variant_counts = 0
	shift = 0
	while shift < len(string) - minimum_sizes[0]:
		if (
				(not "#" == string[shift + len_cluster])  # no spring directly after arrangement
				and (len(clusters_left) > 1 or "#" not in string[shift + len_cluster:])  # no spring after if last arrangement
		):
			variant_counts += get_variant_counts(string[shift + len_cluster + 1:], clusters_left[1:], minimum_sizes[1:])
		if "#" == string[shift]:  # spring in front
			return variant_counts
		if "." == string[shift+len_cluster]:
			shift += len_cluster + 1
		shift += 1
	if shift == len(string) - minimum_sizes[0]:
		if (
				len(clusters_left) > 1 or "#" not in string[shift + len_cluster:]  # no spring after if last arrangement
		):
			variant_counts += get_variant_counts(string[shift + len_cluster + 1:], clusters_left[1:], minimum_sizes[1:])

	return variant_counts

xc
ress = 0
for i, SPRING in enumerate(SPRINGS):
	res = get_variant_counts(*SPRING)
	ress += res
	print(res)
print(ress)
