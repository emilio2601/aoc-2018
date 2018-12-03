import sys
claims = []


board = [[0 for x in range(1000)] for y in range(1000)]

with open("day3", "r") as f:
    for line in f:
        coords = line.split(" ")[2]
        coords = coords.rstrip(":")
        coords = coords.split(",")
        coords = [int(x) for x in coords]

        size = line.split(" ")[3]
        size = [int(x) for x in size.split("x")]
        claims.append([coords, size])

clashes = 0

for claim in claims:
    for x in range(claim[1][0]):
        for y in range(claim[1][1]):
            board[x+claim[0][0]][y+claim[0][1]] += 1

for rowx in board:
    for element in rowx:
            if element >= 2:
                clashes += 1

print(f"Part 1: {clashes}")

for idx, claim in enumerate(claims):
    hasDied = False
    for x in range(claim[1][0]):
        for y in range(claim[1][1]):
            if board[x+claim[0][0]][y+claim[0][1]] != 1:
                hasDied = True
    if not hasDied:
        print(f"Part 2: #{idx+1}")