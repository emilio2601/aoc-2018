
puzzle = ""

with open("day5", "r") as f:
    puzzle = f.read()

#puzzle = "dabAcCaCBAcCcaDA"

def fullyReactPolymer(puzzle):
    actionTaken = True
    transformedPuzzle = ""

    while actionTaken:
        actionTaken = False
        for idx, char in enumerate(puzzle):
            try: 
                nextChar = puzzle[idx+1]

                if char.swapcase() == nextChar:
                    #print(f"removing {char}{nextChar}")
                    actionTaken = True
                    transformedPuzzle += puzzle[idx+2:]
                    break
                else:
                    transformedPuzzle += char
            except IndexError:
                pass

        puzzle = transformedPuzzle
        transformedPuzzle = ""
    
    return len(puzzle)

def fullyReactPolymer2(puzzle):
    actionTaken = True
    transformedPuzzle = ""
    while actionTaken:
        actionTaken = False
        for idx in range(len(puzzle)-1):
            if puzzle[idx].swapcase() == puzzle[idx+1]:
                transformedPuzzle = puzzle[0:idx] + puzzle[idx+2:]
                actionTaken = True
                break
        puzzle = transformedPuzzle
    return len(transformedPuzzle)

print(f"Part 1: {fullyReactPolymer2(puzzle)}")

results = []

for char in "abcdefghijklmnopqrstuvwxyz":
    noLetter = puzzle.replace(char, "").replace(char.upper(), "")
    res = fullyReactPolymer2(noLetter)
    results.append(res)
    print(f"Part 2: without letter {char}: {res}")

print(f"Part 2: {min(results)}")  