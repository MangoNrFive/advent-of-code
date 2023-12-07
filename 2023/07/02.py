from collections import Counter


def get_type(hand):
	counters = Counter(hand)
	try:
		jokers = counters.pop("J")
	except KeyError:
		jokers = 0
	counts = counters.values()

	if len(counts) <= 1:
		return 6  # Five of a kind
	elif len(counts) == 2:
		if max(counts) + jokers == 4:
			return 5  # Four of a kind
		return 4  # Full House
	elif len(counts) == 3:
		if max(counts) + jokers == 3:
			return 3  # Three of a kind
		return 2  # Two pair
	elif len(counts) == 4:
		return 1  # One pair
	return 0  # High card


with open('input2.txt') as f:
	lines = f.readlines()

hands = []
bids = []
types = []
for line in lines:
	h, b = line.split()
	hands.append(h.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "1").replace("T", "A"))
	bids.append(int(b))
	types.append(get_type(h))

res = sum((rank0+1)*bid for rank0, (_, _, bid) in enumerate(sorted(zip(types, hands, bids))))
print(res)
