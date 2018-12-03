import sys

twice  = 0
thrice = 0

lines = []

with open("day2", "r") as f:
    for line in f:
        lines.append(line)

for line in lines:
    hasTwice  = False
    hasThrice = False
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if line.count(letter) == 2:
            if not hasTwice:
                twice += 1
                hasTwice = True
            
        if line.count(letter) == 3:
            if not hasThrice:
                thrice += 1
                hasThrice= True

print(f"Part 1: {twice * thrice}")

for line in lines:
    for line2 in lines:
        differentChars = 0
        for idx, char in enumerate(line):
            if char != line2[idx]:
                differentChars += 1
                if differentChars > 2:
                    break
        if differentChars == 1:
            answer = ""
            for idx, char in enumerate(line):
                if char == line2[idx]:
                    answer += char
            print(f"Part 2: {answer}")
            sys.exit()