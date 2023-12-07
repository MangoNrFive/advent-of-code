from collections import Counter


def get_type(hand):
	counts = Counter(hand).values()
	if len(counts) == 1:
		return 6  # Five of a kind
	elif len(counts) == 2:
		if max(counts) == 4:
			return 5  # Four of a kind
		return 4  # Full House
	elif len(counts) == 3:
		if max(counts) == 3:
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
	hands.append(h.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "B").replace("T", "A"))
	bids.append(int(b))
	types.append(get_type(h))

res = sum((rank0+1)*bid for rank0, (_, _, bid) in enumerate(sorted(zip(types, hands, bids))))
print(res)
