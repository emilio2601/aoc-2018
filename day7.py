from collections import defaultdict

reqs  = []
steps = set()


with open("day7", "r") as f:
    for line in f:
        prereq = line.split(" ")[1]
        goal   = line.split(" ")[7]
        steps.add(prereq)
        steps.add(goal)
        reqs.append((prereq, goal))

order = ""
steps2 = set(steps)

while steps:
    available = list(steps)
    for req in reqs:
        if req[1] in steps and req[0] in steps:
            try:
                available.remove(req[1])
            except ValueError:
                pass
    to_remove = min(available)
    order += to_remove
    steps.remove(to_remove)

print(f"Part 1: {order}")

workers = ["idle", "idle", "idle", "idle", "idle"]
ctr = 0
order2 = ""

while steps2:
    ctr += 1
    for idx, worker in enumerate(workers):
        if worker != "idle":
            workers[idx][0] = workers[idx][0] - 1
            if workers[idx][0] == 0:
                order2 += workers[idx][1]
                steps2.remove(workers[idx][1])
                workers[idx] = "idle"

    available = sorted(list(steps2))
    for req in reqs:
        if req[1] in steps2 and req[0] in steps2:
            try:
                available.remove(req[1])
            except ValueError:
                pass
    for step_a in available:
        for idx, worker in enumerate(workers):
            if worker == "idle":
                if step_a not in [x[1] for x in workers]:
                    workers[idx] = [ord(step_a) - 4, step_a]

print(f"Part 2: {ctr-1}")
