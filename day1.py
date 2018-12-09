counter = 0
history = [counter]
nums = []

with open("day1", "r") as f:
    for line in f:
        nums.append(int(line)) 

firstRun = True
notFound = True

while notFound:
    for num in nums:
        counter += num
        if (counter in history) and notFound:
            print(f"Part 2: {counter}")
            notFound = False
        history.append(counter)
    
    if firstRun:
        print(f"Part 1: {counter}")
        firstRun = False
