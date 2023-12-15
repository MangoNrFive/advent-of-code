def get_maximum_loc(string, clusters):
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

	return [len(string) - e for e in r_minimum_sizes[::-1]]


with open('input2.txt') as f:
	lines = f.readlines()

SPRINGs = []
for line in lines:
	s, a = line.strip().split()
	s = ",".join([s]*5)
	a = ",".join([a]*5)
	a = [int(e) for e in a.split(",")]
	m = get_maximum_loc(s, a)
	SPRINGs.append((s, a, m))


total = 0
for STRING, CLUSTERs, MAXIMUM_LOCs in SPRINGs:
	print()
	print()
	print()
	print(CLUSTERs)
	print(MAXIMUM_LOCs)
	print(STRING)
	loc_counts = {0: 1}
	for CLUSTER, MAXIMUM_LOC in zip(CLUSTERs[:-1], MAXIMUM_LOCs[:-1]):
		loc_counts_new = {}
		for loc, count in loc_counts.items():
			print(" "*loc + "|")
			for shift in range(MAXIMUM_LOC - loc+1):
				if "#" in STRING[loc:loc + shift]:  # spring in front of arrangement
					print("_"*loc + "-"*shift + "^"*CLUSTER + " spring in front")
					break
				if "." in STRING[loc + shift:loc + shift + CLUSTER]:  # hole in arrangement
					print("_"*loc + "-"*shift + "^"*CLUSTER + " hole in arrangement")
					continue
				if "#" in STRING[loc + shift + CLUSTER:loc + shift + CLUSTER + 1]:  # spring directly at end of arrangement
					print("_"*loc + "-"*shift + "^"*CLUSTER + " spring directly after")
					continue
				print("_"*loc + "-"*shift + "^"*CLUSTER + " valid")
				new_loc = loc + shift + CLUSTER + 1
				if new_loc in loc_counts_new:
					loc_counts_new[new_loc] += count
				else:
					loc_counts_new[new_loc] = count
			print(loc_counts_new)
		loc_counts = loc_counts_new.copy()
		print()

	CLUSTER = CLUSTERs[-1]
	MAXIMUM_LOC = MAXIMUM_LOCs[-1]
	loc_counts_new = {}
	for loc, count in loc_counts.items():
		print(" " * loc + "|")
		for shift in range(MAXIMUM_LOC - loc+1):
			if "#" in STRING[loc:loc + shift]:  # spring in front of arrangement
				print("_" * loc + "-" * shift + "^" * CLUSTER + " spring in front")
				break
			if "." in STRING[loc + shift:loc + shift + CLUSTER]:  # hole in arrangement
				print("_" * loc + "-" * shift + "^" * CLUSTER + " hole in arrangement")
				continue
			if "#" in STRING[loc + shift + CLUSTER:]:  # spring after arrangement
				print("_" * loc + "-" * shift + "^" * CLUSTER + " spring after arrangement")
				continue
			print("_" * loc + "-" * shift + "^" * CLUSTER + " valid")
			new_loc = loc + shift + CLUSTER + 1
			if new_loc in loc_counts_new:
				loc_counts_new[new_loc] += count
			else:
				loc_counts_new[new_loc] = count
	loc_counts = loc_counts_new.copy()
	print(loc_counts)
	print(sum(loc_counts.values()))
	total += sum(loc_counts.values())
print(total)
