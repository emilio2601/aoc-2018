

plants = ["." for x in range(200)]

rules  = set()

with open("day12", "r") as f:
    for line in f:
        if line.split(" ")[0] == "initial":
            for idx, plant in enumerate(line.split(" ")[2].rstrip("\n")):
                plants[idx+50] = plant
        elif line != "\n":
            if line.split(" ")[2].rstrip("\n") == "#":
                rules.add(line.split(" ")[0])

def find_part1(plants):
    ctr = 0
    for idx, plant in enumerate(plants):
        if plant == "#":
            ctr += idx - 50
    return ctr

res = 0

for i in range(1,21):
    newplants = ["." for x in range(200)]
    
    for idx in range(2,190):
        if "".join(plants[idx-2:idx+3]) in rules:
            newplants[idx] = "#"
    
    plants = newplants
    board_print = "".join(plants[47:100])
    newres = find_part1(plants)
    print(f"{i}: {board_print} ctr: {newres} dc: {res - newres}")
    res = newres


print(f"Part 1: {find_part1(plants)}")
print(f"Part 2: {int(6855 + ((5e10 - 100) * 62))}")