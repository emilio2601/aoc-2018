from collections import defaultdict
import math
from tqdm import tqdm

board = [[0 for x in range(400)] for y in range(400)]

coords = []

with open("day6", "r") as f:
    for line in f:
        coords.append([int(x) for x in line.split(",")])

for xidx, x in tqdm(enumerate(board)):
    for yidx, y in enumerate(x):
        if [xidx, yidx] in coords:
            board[xidx][yidx] = "N"
        else:
            winning_coords = defaultdict(int)
            for idx, coord in enumerate(coords):
                distance = abs(coord[0] - xidx) + abs(coord[1] - yidx)
                winning_coords[idx] = distance
            min_distance = min(winning_coords.values())
            if list(winning_coords.values()).count(min_distance) != 1:
                board[xidx][yidx] = "N"
            else:
                for k, v in winning_coords.items():
                    if v == min_distance:
                        board[xidx][yidx] = (min_distance, k)

winning_coords = defaultdict(lambda:1)

for xidx, x in enumerate(board):
    for yidx, y in enumerate(x):
        if y != "N":
            winning_coords[y[1]] += 1
            if xidx == 0 or yidx == 0 or xidx == 399 or yidx == 399:
                winning_coords[y[1]] -= 1e7

print(f"Part 1: {max([x[1] for x in winning_coords.items()])}")

board = [[0 for x in range(400)] for y in range(400)]

for xidx, x in tqdm(enumerate(board)):
    for yidx, y in enumerate(x):
        for coord in coords:
            board[xidx][yidx] += abs(coord[0] - xidx) + abs(coord[1] - yidx)

ctr = 0
for xidx, x in enumerate(board):
    for yidx, y in enumerate(x):
        if y < 10000:
            ctr += 1

print(f"Part 2: {ctr}")