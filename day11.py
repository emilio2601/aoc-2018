from tqdm import tqdm
import numpy as np

serial = 9810

board = np.zeros((300, 300), dtype=np.int32)

for xidx, x in enumerate(board):
    for yidx, y in enumerate(x):
        power = (((xidx + 10) * yidx) + serial) * (xidx + 10)
        try:
            power = int(str(power)[-3])
        except:
            power = 0
        board[xidx][yidx] = power - 5

maxval_pt1     = 0
max_coords_pt1 = (0, 0)

maxval_pt2     = 0
max_coords_pt2 = (0, 0)

for x in tqdm(range(300)):
    for y in range(300):
        limit = max([x, y])

        acc = 0

        for size in range(1, (300-limit)):
            if size > 20:
                break
            acc = 0
            for subrow in range(size):
                acc += np.sum(board[x+subrow][y:y+size])
            
            if size == 3:
                if acc > maxval_pt1:
                    maxval_pt1 = acc
                    max_coords_pt1 = (x, y)
            
            if acc > maxval_pt2:
                maxval_pt2 = acc
                max_coords_pt2 = (x, y, size)


print(f"Part 1: {max_coords_pt1}")
print(f"Part 2: {max_coords_pt2}")