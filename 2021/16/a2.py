import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import binascii


def main(file):
	with open(file) as f:
		transmission_hex = f.readlines()[0]
	transmission_bin = format(int(transmission_hex, 16), f"0>{len(transmission_hex)*4}b")

	print("\n" + "#"*80)
	print(file)

	_, value = decode_packet(transmission_bin)
	print(f"{value=}")


def decode_packet(bits):
	print("-"*80)
	version_bin, bits = bits[:3], bits[3:]
	version = int(version_bin, 2)
	print(f"{version=}")

	type_ID_bin, bits = bits[:3], bits[3:]
	type_ID = int(type_ID_bin, 2)
	print(f"{type_ID=}")

	if type_ID == 4:  # literal value packet
		literal_value_bin = ""
		while True:
			group_flag, bits = bits[:1], bits[1:]
			literal_value_bin_next, bits = bits[:4], bits[4:]
			literal_value_bin += literal_value_bin_next
			if group_flag == "0":
				break

		literal_value = int(literal_value_bin, 2)
		print(f"{literal_value=}")

	else:  # operator packet
		length_type_ID, bits = bits[:1], bits[1:]
		sub_values = []
		if length_type_ID == "0":  # next 15 bits -> total length in bits of sub-packets
			total_length_bin, bits = bits[:15], bits[15:]
			total_length = int(total_length_bin, 2)
			print(f"{total_length=}")

			bits_sub, bits = bits[:total_length], bits[total_length:]
			while bits_sub:
				bits_sub, sub_value = decode_packet(bits_sub)
				sub_values.append(sub_value)


		else:  # next 11 bits -> number of sub-packets immediately contained by packet
			num_sub_packets_bin, bits = bits[:11], bits[11:]
			num_sub_packets = int(num_sub_packets_bin, 2)
			print(f"{num_sub_packets=}")

			for _ in range(num_sub_packets):
				bits, sub_value = decode_packet(bits)
				sub_values.append(sub_value)

	if type_ID == 0:
		value = sum(sub_values)
	elif type_ID == 1:
		value = math.prod(sub_values)
	elif type_ID == 2:
		value = min(sub_values)
	elif type_ID == 3:
		value = max(sub_values)
	elif type_ID == 4:
		value = literal_value
	elif type_ID == 5:
		value = int(sub_values[0] > sub_values[1])
	elif type_ID == 6:
		value = int(sub_values[0] < sub_values[1])
	elif type_ID == 7:
		value = int(sub_values[0] == sub_values[1])
	else:
		raise Exception

	return bits, value


main("example2_0.txt")
main("example2_1.txt")
main("example2_2.txt")
main("example2_3.txt")
main("example2_4.txt")
main("example2_5.txt")
main("example2_6.txt")
main("example2_7.txt")
main("input.txt")
