from functools import reduce
from math import gcd

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]


instructions = lines[0]

pos_dict = {}
for l in lines[2:]:
    splited = l.strip(")").split(" = (")
    pos_dict[splited[0]] = splited[1].split(", ")

first_pos = lines[2].split(" = (")[0]


i = 0
pos = "AAA"
while True:
    pos = pos_dict[pos][0 if instructions[i % len(instructions)] == "L" else 1]
    i += 1
    if pos == "ZZZ":
        break

print("p1", i)

pos_a = [p for p in pos_dict.keys() if p[2] == "A"]
pos_a_dict = {}

for start_pos in pos_a:
    pos = start_pos
    i = 0

    while True:
        pos = pos_dict[pos][0 if instructions[i % len(instructions)] == "L" else 1]
        i += 1
        if pos[2] == "Z":
            break
    pos_a_dict[start_pos] = i

pos_a_list = list(pos_a_dict.values())
lcm = 1
for a in pos_a_list:
    lcm = lcm * a // gcd(lcm, a)
print("p2", lcm)
