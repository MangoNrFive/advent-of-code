import numpy as np
import math


def main(file):
	with open(file) as f:
		lines = f.readlines()

	input_str = "".join(lines)
	arr = input_str.split("\n\n")

	draws = arr[0].split(",")
	draws = [int(draw) for draw in draws]


	arr = arr[1:]
	boards = []
	for board in arr:
		boards.append(np.resize(np.fromstring(board, dtype=int, sep=' '), (5,5)))

	current_boards = boards[:]
	draw_idx = 0
	while current_boards:
		realized_draws = draws[:draw_idx]
		for board_idx, board in enumerate(current_boards):
			for row_idx in range(5):
				bingo = True
				for column_idx in range(5):
					if not board[row_idx, column_idx] in realized_draws:
						bingo = False
				if bingo == True:
					del current_boards[board_idx]

		for board_idx, board in enumerate(current_boards):
			for column_idx in range(5):
				bingo = True
				for row_idx in range(5):
					if not board[row_idx, column_idx] in realized_draws:
						bingo = False
				if bingo == True:
					del current_boards[board_idx]

		draw_idx += 1
	return realized_draws, board

#main("input.txt")
realized_draws, board = main("example.txt")

board_list = list(np.ndarray.tolist(board.flatten()))
board_list = [element for element in board_list if element not in realized_draws]
print(sum(board_list) * realized_draws[-1])
