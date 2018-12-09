from collections import defaultdict
from tqdm import tqdm
import sys

guard_events = []
lines = []


with open("day4", "r") as f:
    for line in f:
        lines.append(line)

lines.sort()


for line in lines:
        split = line.split(" ")
        date = split[0][1:]
        time = int(split[1].rstrip("]").split(":")[1])
        if split[2] == "wakes":
            guard_events.append((time, "wakes up"))

        if split[2] == "falls":
            guard_events.append((time, "falls asleep"))
        
        if split[2] == "Guard":
            guard_events.append((time, split[3]))



guard = ""
time_start = 0
minutes = defaultdict(int)
guards = defaultdict(int)

for event in guard_events:
    if event[1] == "falls asleep":
        time_start = event[0]

    elif event[1] == "wakes up":
        guards[guard] += event[0] - time_start
        for x in range(time_start, event[0]):
            minutes[(guard, x)] += 1
    else:
        guard = event[1]

def argmax(d):
     best = None
     for k,v in d.items():
         if best is None or v > d[best]:
             best = k
     return best

best_guard = argmax(guards)
guard_minutes = defaultdict(int)

for k,v in minutes.items():
    if k[0] == best_guard:
        guard_minutes[k] = v

part1 = int(argmax(guard_minutes)[0].lstrip("#")) * argmax(guard_minutes)[1]
part2 = int(argmax(minutes)[0].lstrip("#")) * argmax(minutes)[1]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")