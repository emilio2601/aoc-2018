import sys
import numpy as np
from tqdm import tqdm

particles = []

with open("day10", "r") as f:
    for line in f:
        pos, vel = line.split("v")
        pos = pos[10:].strip("> ").split(",")
        vel = vel[9:].strip(">\n").split(",")
        particles.append([[int(x) for x in pos], [int(x) for x in vel]])

def print_board(particles, ctr):
    with open(f"{ctr}.pbm", "w") as f:
        minw = min([x[0][0] for x in particles])
        minh = min([x[0][1] for x in particles])

        maxw = max([x[0][0] for x in particles])
        maxh = max([x[0][1] for x in particles])

        width  = abs(maxw) + abs(minw)
        height = abs(maxh) + abs(minh)
        
        board = [[" " for x in range(height)] for y in range(width)]
        
        f.write("P1\n")
        f.write(f"{width} {height}\n")

        for p in particles:
            board[p[0][1]][p[0][0]] = "#"
        
        for row in board:
            if "#" in row:
                print("".join(row).lstrip(" ").rstrip(" "))
            

ctr = 0

while True:
    ctr += 1
    for idx, particle in enumerate(particles):
        particles[idx][0] = [ particles[idx][0][0] + particles[idx][1][0], particles[idx][0][1] + particles[idx][1][1] ]

    if ctr == 10813:
        print("Part 1: ")
        print_board(particles,ctr)
        print("Part 2: 10813")
        sys.exit()