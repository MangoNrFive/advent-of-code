import numpy as np
import math
from statistics import median
from collections import defaultdict, Counter
import binascii


version_sum = None


def main(file):
	with open(file) as f:
		transmission_hex = f.readlines()[0]
	transmission_bin = format(int(transmission_hex, 16), f"0>{len(transmission_hex)*4}b")

	print("\n" + "#"*80)
	print(file)

	global version_sum
	version_sum = 0
	decode_packet(transmission_bin)
	print(f"{version_sum=}")


def decode_packet(bits):
	global version_sum

	print("-"*80)
	version_bin, bits = bits[:3], bits[3:]
	version = int(version_bin, 2)
	print(f"{version=}")
	version_sum += version

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
		if length_type_ID == "0":  # next 15 bits -> total length in bits of sub-packets
			total_length_bin, bits = bits[:15], bits[15:]
			total_length = int(total_length_bin, 2)
			print(f"{total_length=}")

			bits_sub, bits = bits[:total_length], bits[total_length:]
			while bits_sub:
				bits_sub = decode_packet(bits_sub)


		else:  # next 11 bits -> number of sub-packets immediately contained by packet
			num_sub_packets_bin, bits = bits[:11], bits[11:]
			num_sub_packets = int(num_sub_packets_bin, 2)
			print(f"{num_sub_packets=}")

			for _ in range(num_sub_packets):
				bits = decode_packet(bits)

	return bits


main("example_0.txt")
main("example_1.txt")
main("example_2.txt")
main("example_3.txt")
main("example_4.txt")
main("example_5.txt")
main("example_6.txt")
main("input.txt")
