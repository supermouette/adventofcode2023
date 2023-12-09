from time import time

t0 = time()
with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

seeds = lines[0].split(": ")[1].split(" ")

ranges = []

for line in lines[1:]:
    if line == "":
        continue
    if "map" in line:
        ranges.append([])
    else:
        ranges[-1].append([int(i) for i in line.split(" ")])

min_location = 99999999999999  # this should be the biggest number ever, right ?

for seed in seeds:
    id = int(seed)
    for r in ranges:
        for r0, r1, r2 in r:
            if r1 <= id <= r1 + r2:
                id = id - r1 + r0
                break
    min_location = min(min_location, id)

print(min_location)

min_location = 99999999999999  # this should be the biggest number ever, right ?


for i in range(0, len(seeds), 2):
    shortcut = [0] * len(ranges)
    print("seeds", seeds[i : i + 2])

    for j in range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])):
        id = j
        for s, r in enumerate(ranges):
            r0, r1, r2 = r[shortcut[s]]
            if r1 <= id < r1 + r2:
                id = id - r1 + r0
            else:
                for i, (r0, r1, r2) in enumerate(r):
                    if r1 <= id < r1 + r2:
                        id = id - r1 + r0
                        shortcut[s] = i
                        break
        min_location = min(min_location, id)

print(min_location)  # took 5H30 # took 1H50 after adding "shortcuts"
print(time() - t0)
