from collections import deque

nums = []

with open("day8", "r") as f:
    for num in f.read().split(" "):
        nums.append(int(num))

part1 = deque(nums)
ctr = 0

def parse_part1(nodes):
    global ctr
    child    = part1.popleft()
    metadata = part1.popleft()

    for x in range(child):
        parse_part1(part1)

    for y in range(metadata):
        entry = part1.popleft()
        ctr += entry

parse_part1(part1)
print(f"Part 1: {ctr}")

part2 = deque(nums)
ctr = 0

def parse_part2(nodes):
    child    = part2.popleft()
    metadata = part2.popleft()
    value = 0
    child_vals = []

    for x in range(child):
        child_vals.append(parse_part2(part2))

    for y in range(metadata):
        entry = part2.popleft()
        if child == 0:
            value += entry
        else:
            try:
                value += child_vals[entry-1]
            except IndexError:
                pass
    
    return value

print(f"Part 2: {parse_part2(part2)}")