import numpy as np


with open('input2.txt') as f:
	lines = f.readlines()

FIELD = []
for line in lines:
	FIELD.append(list(line.strip()))
FIELD = np.array(FIELD, dtype=int)
FIELD = np.pad(FIELD, [(1, 1), (1, 1)], mode='constant', constant_values=np.iinfo(np.int32).max//2)

init = np.full_like(FIELD, np.iinfo(np.int32).max//2, dtype=int)
heat_loss_map = np.broadcast_to(init[..., None], init.shape+(11,))
heat_loss_map = np.broadcast_to(heat_loss_map[..., None], heat_loss_map.shape+(4,)).copy()
heat_loss_map[1, 1, 0, :] = 0

FIELD = np.broadcast_to(FIELD[..., None], FIELD.shape+(11,))
FIELD = np.broadcast_to(FIELD[..., None], FIELD.shape+(4,)).copy()

while True:
	heat_loss_map_last = heat_loss_map.copy()

	# north
	heat_loss_map[:-1, :, 1:, 0] = np.minimum(heat_loss_map[:-1, :, 1:, 0], heat_loss_map[1:, :, :-1, 0] + FIELD[:-1, :, 1:, 0])
	heat_loss_map[:-1, :, 1, 0] = np.minimum(heat_loss_map[:-1, :, 1, 0], np.min(heat_loss_map[1:, :, 4:, 2:], axis=(2, 3)) + FIELD[:-1, :, 1, 0])

	# south
	heat_loss_map[1:, :, 1:, 1] = np.minimum(heat_loss_map[1:, :, 1:, 1], heat_loss_map[:-1, :, :-1, 1] + FIELD[1:, :, 1:, 1])
	heat_loss_map[1:, :, 1, 1] = np.minimum(heat_loss_map[1:, :, 1, 1], np.min(heat_loss_map[:-1, :, 4:, 2:], axis=(2, 3)) + FIELD[1:, :, 1, 1])

	# east
	heat_loss_map[:, 1:, 1:, 2] = np.minimum(heat_loss_map[:, 1:, 1:, 2], heat_loss_map[:, :-1, :-1, 2] + FIELD[:, 1:, 1:, 2])
	heat_loss_map[:, 1:, 1, 2] = np.minimum(heat_loss_map[:, 1:, 1, 2], np.min(heat_loss_map[:, :-1, 4:, :2], axis=(2, 3)) + FIELD[:, 1:, 1, 2])

	# west
	heat_loss_map[:, :-1, 1:, 3] = np.minimum(heat_loss_map[:, :-1, 1:, 3], heat_loss_map[:, 1:, :-1, 3] + FIELD[:, :-1, 1:, 3])
	heat_loss_map[:, :-1, 1, 3] = np.minimum(heat_loss_map[:, :-1, 1, 3], np.min(heat_loss_map[:, 1:, 4:, :2], axis=(2, 3)) + FIELD[:, :-1, 1, 3])

	if np.array_equal(heat_loss_map, heat_loss_map_last):
		break

print(np.min(heat_loss_map[:, :, 4:, :], axis=(2, 3))[-2, -2])
